import { useState } from 'react';
import './App.css';
import "tachyons"

function App() {
  // define the use state
  const [languages, setLanguages] = useState([
    {name: "Php", votes: 0},
    {name: "Python", votes: 0},
    {name: "JavaSript", votes: 0},
    {name: "Java", votes: 0}
  ]);

  const addVotes = (lang) => {
    lang.votes++;
    console.log(languages);
    setLanguages([...languages]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h2>Vote You Language</h2>
        {
          languages.map((language, index) => {
            return (
              <ul className="list pl0 ml0 center mw5 ba b--light-silver br3">
                <li className="ph3 pv2 bb b--light-silver" key={index}>
                  {language.votes} {language.name}
                  <button className="f6 grow no-underline br-pill ba ph3 pv2 mb2 dib dark-green" onClick={() => addVotes(language)}>Click Here</button>
                </li>
            </ul>
            )
          }
        )}
      </header>
    </div>
  );
}

export default App;
