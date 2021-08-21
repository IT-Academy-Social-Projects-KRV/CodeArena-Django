# get python image
FROM python:latest

# make directory and go inside it
RUN mkdir -p /usr/src/api
WORKDIR /usr/src/api

# copy django file to image
COPY ./codeArena .
COPY ./requirements.txt .
COPY ./bin/api-entrypoint.sh .

# install all python packages
RUN pip install --no-cache-dir -r requirements.txt

# entry point for api container
ENTRYPOINT [ "sh", "api-entrypoint.sh" ]