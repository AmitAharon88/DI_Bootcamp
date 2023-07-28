import React from 'react';
import quotes from './components/QuotesDatabase';
import colors from './components/ColorDatabase';
import { useState } from 'react';
import './App.css';

function App() {
  const [container, setContainer] = useState({
    currentQuoteIndex: 0,
    color: "#FF6633",
  });
  

  const colorChange = () => {
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    if (container.color === randomColor) {
      colorChange()
    } else {
      setContainer(prevConatiner => ({
        ...prevConatiner,
        color: randomColor,
      }));
    };
  };

  const quoteChange = () => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    if (container.currentQuoteIndex === randomIndex) {
      quoteChange()
    } else {
      setContainer(prevConatiner => ({
        ...prevConatiner,
        currentQuoteIndex: randomIndex
      }));
    };
  };

  const handelClick = () => {
    colorChange();
    quoteChange();
  };

  const { currentQuoteIndex, color } = container;
  const { quote, author } = quotes[currentQuoteIndex];
 
  return (
    <div className="App" style={{ backgroundColor: color }}>
      <header className="App-header">
        <div className="container" style={{ backgroundColor: "white" }}>
          <h1 style={{ color }}>{quote}</h1>
          {author && <p style={{ color }}>- {author}</p>}
          <button onClick={handelClick} style={{ backgroundColor: color }}>New quote</button>
        </div>
      </header>
    </div>
  );
};

export default App;
