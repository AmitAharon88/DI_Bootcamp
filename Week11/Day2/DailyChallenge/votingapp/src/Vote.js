import React from "react";

class Vote extends React.Component {
    constructor() {
        super();
        // define the state object
        this.state = {
            languages : [
                {name: "Php", votes: 0},
                {name: "Python", votes: 0},
                {name: "JavaSript", votes: 0},
                {name: "Java", votes: 0}
            ]
        };
    };

    addVotes = (lang) => {
        lang.votes++;
        console.log(this.state.languages);
        this.setState({languages : [...this.state.languages]})
    };

    render () {
        return (
            <div className="App">
              <header className="App-header">
                <h2>Vote You Language</h2>
                {
                  this.state.languages.map((language, index) => {
                    return (
                      <ul className="list pl0 ml0 center mw5 ba b--light-silver br3">
                        <li className="ph3 pv2 bb b--light-silver" key={index}>
                          {language.votes} {language.name}
                          <button className="f6 grow no-underline br-pill ba ph3 pv2 mb2 dib dark-green" onClick={() => this.addVotes(language)}>Click Here</button>
                        </li>
                    </ul>
                    )
                  }
                )}
              </header>
            </div>
        );
    }
}

export default Vote;