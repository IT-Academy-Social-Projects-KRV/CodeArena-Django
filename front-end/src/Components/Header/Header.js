import React from 'react';
import Navigation from './Navigation';
import './header.css';
import { BrowserRouter as Router, Switch, Route, } from "react-router-dom"

import MainContainer from '../pages/homePage/MainContainer';
import NewsPage from '../pages/newsPage/NewsPage';
import VacanciesPage from '../pages/vacanciesPage/VacanciesPage';

function Header() {
    return (
        <>
            <header className="header type">
                <section className="top_menu">
                    <div>
                        <button>Sign Up</button>
                        <button>Log In</button>
                    </div>
                </section>
                <div className="mainheader type">
                <h3><b><nav className="main_navigation type" font-size="2">
                        <a href="/">Code Arena</a>
                    </nav></b></h3>
                    <Navigation />
                </div>
            </header>
            <Router>
                <Switch>
                    <Route exact path="/" component={MainContainer} />
                    <Route exact path="/news" component={NewsPage} />
                    <Route exact path="/jobs" component={VacanciesPage}/>
                </Switch>
            </Router>
        </>
    )
}

export default Header;
