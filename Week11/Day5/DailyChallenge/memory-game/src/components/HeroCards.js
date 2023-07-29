import heroes from '../superheroes.json';
import NavBar from './NavBar';
import { useState } from 'react';
import './HeroCards.css';

const HeroCards = () => {
    const [score, setScore] = useState(0);
    const [topScore, setTopScore] = useState(0);
    const [clickedHeroes, setClickedHeroes] = useState([]);
    const [cardOrder, setCardOrder] = useState(heroes.superheroes);
    
    const handelClick = (id) => {
        if (clickedHeroes.includes(id)) {
            if (topScore < score) {
                setTopScore(score);
            }
            setScore(0);
            setClickedHeroes([]);
        } else {
            setScore(score + 1);
            setClickedHeroes(prevHeroes => 
                [...prevHeroes, id]
            );
        };
        shuffle();
    };

    const shuffle = () => {
        const shuffledCards = heroes.superheroes.sort(() => Math.random() - 0.5);
        setCardOrder(shuffledCards);
    };

    return (
        <>
        <NavBar score={score} topScore={topScore}/>
        <div className='container'>
            {
                cardOrder.map((hero) => {
                    return (
                        <div key={hero.id} className='card' onClick={() => handelClick(hero.id)}>
                            <img style={{height:"200px"}} src={hero.image} alt={hero.name} />
                            <p><b>Name:</b> {hero.name}</p>
                            <p><b>Occupation:</b> {hero.occupation}</p>
                        </div>
                    )
                })
            }
        </div> 
        </>
    )
};

export default HeroCards