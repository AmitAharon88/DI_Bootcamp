import { useState } from 'react';
import './NavBar.css';
const NavBar = (props) => {

    return (
        <nav >
            <div className="topNav">
                <h1>Superheroes Memory Game</h1>
                <div className="counter">
                    <h3>Score: {props.score}</h3>
                    <h3>Top Score: {props.topScore}</h3>
                </div>
            </div>
            <hr/>
            <h2 className="subNav">Get points by clicking on an image but don't click on any more than once!</h2>
        </nav>
    )
}

export default NavBar