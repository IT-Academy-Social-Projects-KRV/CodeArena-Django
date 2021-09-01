import React, { Component } from 'react';
import Navigation from '../Header/Navigation';
import { Navbar, Nav, Button } from 'react-bootstrap';
import { BrowserRouter as Router, Switch, Route,  } from "react-router-dom"


import MainContainer from '../pages/homePage/MainContainer';
import CreatePage from '../pages/createtaskPage/CreatePage';
import NewsPage from '../pages/newsPage/NewsPage';

export default class Auth_Header extends Component {
    render() {
        return (
            <>
                <header className="header">
                    <section className="top_menu">
                        <div>
                            <Navbar collapseOnSelect expand="rg" className="grey" variant="dark">
                                <Navbar.Brand className="ms-3" >  </Navbar.Brand>
                                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                                <Navbar.Collapse id="responsive-navbar-nav">
                                    <Nav className="m-2">
                                        <Nav.Link href="/" >Home </Nav.Link>
                                        <Nav.Link href="profile" >Profile </Nav.Link>
                                        <Nav.Link href="/list_competitions">List of competitions</Nav.Link>
                                        <Nav.Link href="/list_vacancies">Vacancies list</Nav.Link>
                                        <Nav.Link href="/creating_task">Creating task</Nav.Link>


                                    </Nav>
                                    <Nav.Link href="exit" className="ms-auto">
                                        <Button variant="danger" className="me-2" >sign out</Button >
                                    </Nav.Link>
                                </Navbar.Collapse>
                            </Navbar>
                        </div>
                    </section>
                    <div className="mainheader">
                    <h3><b><nav className="main_navigation" font-size="2">
                        <a href="/">Code Arena</a>
                    </nav></b></h3>
                        <Navigation />
                    </div>
                </header>
                <Router>
                    <Switch>
                        <Route exact path="/" component={MainContainer} />
                        <Route exact path="/creating_task" component={CreatePage} />
                        <Route exact path="/news" component={NewsPage} />
                    </Switch>
                </Router>
            </>
        )
    }
}
