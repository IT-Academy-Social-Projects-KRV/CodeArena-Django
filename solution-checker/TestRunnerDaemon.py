import logging
import os
import subprocess
import sys
import tempfile

from decouple import config
from bson.objectid import ObjectId
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient
from threading import Lock

# Configuration for log output
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('test_runner_logs.log')
file_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


class BaseSolutionChecker:
    """
    This class to check solutions for correctness.

    It is intended to be subclassed.
    """

    def __init__(self, solution, test_cases):
        """
        Initialize the object and create a temporary file
        """

        self.solution = solution
        self.test_cases = test_cases

        with tempfile.NamedTemporaryFile(delete=False) as fp:
            self.fp = fp
            fp.write(solution.encode())
            fp.write('\n'.encode())
            fp.write(test_cases.encode())

    def is_solution_ok(self):
        """
        Check solution for correctness.
        """

        raise NotImplementedError

    def remove_temp_file(self):
        """
        Remove the temporary file
        """

        os.unlink(self.fp.name)


class PythonSolutionChecker(BaseSolutionChecker):
    """
    Check solutions written in Python.
    """

    def is_solution_ok(self):
        """
        Override BaseSolutioChecker.is_solution_ok().
        """

        proces = subprocess.run(['python3', self.fp.name])
        self.remove_temp_file()
        return not proces.returncode


class TestRunnerDaemon:
    """
    This class is the solutions checking service.

    It looks for solutions to be checked,
    checks their correctness, and changes their status respectively.
    """

    def __init__(self, db, thread_workers=10):
        self.db = db
        self.thread_workers = thread_workers
        self.threadlock = Lock()

    def check_solution(self, solution):
        """
        Work on the solution in a separate thread

        Change solution status to 'CR' (correct) or 'FL' (failed)
        """

        task = self.db.task_task.find({'_id': ObjectId(solution['task'])})[0]
        language = task['languages'][0]
        test = task['unit_test']

        checker = LANGUAGE_MAPPING[language](
            solution['solution'],
            test)

        status = 'CR' if checker.is_solution_ok() else 'FL'

        db.task_codertask.update_one(
            {'_id': solution['_id']},
            {'$set': {'status': status}},
        )

    def run(self):
        """
        Start the continuous checking service.
        """

        with ThreadPoolExecutor(max_workers=self.thread_workers) as executor:
            while True:
                solutions = self.db.task_codertask.find({'status': 'ED'})

                for solution in solutions:
                    self.threadlock.acquire()

                    # Change solution status to 'TS' (testing) before solving
                    db.task_codertask.update_one(
                        {'_id': solution['_id']},
                        {'$set': {'status': 'TS'}},
                    )
                    logging.info(f'Solution {solution["_id"]} prepared')

                    self.threadlock.release()

                    executor.submit(self.check_solution, solution)


if __name__ == '__main__':
    LANGUAGE_MAPPING = {"Python": PythonSolutionChecker}
    MONGODB_USER = config("MONGODB_USER")
    MONGODB_USER_PASS = config("MONGODB_USER_PASS")
    MONGODB_HOST = config("MONGODB_HOST")

    url = f'mongodb://{MONGODB_USER}:{MONGODB_USER_PASS}@{MONGODB_HOST}/admin?retryWrites=true&w=majority'
    db = MongoClient(url).codearena_mdb

    TestRunnerDaemon(db).run()
