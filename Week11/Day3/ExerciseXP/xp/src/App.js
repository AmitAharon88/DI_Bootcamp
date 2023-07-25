import React from 'react'
import ErrorBoundary from './ErrorBoundary.js'
import Color from './components/Color.js'
import Child from './components/Color.js'
import './App.css';

class BuggyCounter extends React.Component {
  constructor() {
    super();
    this.state = {counter: 0};
  };

  handelClick = () => {
    // this.setState({ counter : this.state.counter + 1 });
      this.setState((prevState) => ({ 
        counter: prevState.counter + 1 
      }));
  };
  

  render () {
    if (this.state.counter > 5) {
      throw new Error("Count went above 5. NOT ALLOWED")
    } else {
      return (
        <div onClick={this.handelClick}>
          <p>{this.state.counter}</p>
        </div>
      );
    };
  };
};


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <Color>
          <Child />
        </Color>
      </header>
    </div>
  );
}

export default App;
