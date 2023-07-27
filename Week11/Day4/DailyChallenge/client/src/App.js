
import React from 'react';
import './App.css';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      message: '',
      form: '',
      serverResponse: ''
    };
  };

  componentDidMount() {
    this.handelFetch()
  };

  handelFetch = async() => {
    try {
      const res = await fetch('http://localhost:3000/api/hello');
      const data = await res.json();
      console.log(data);
      this.setState({message:data});
    } catch(e) {
      console.log(e);
    }
  };

  handelChange = (event) => {
    this.setState({form: event.target.value})
  };

  handelSumit = async (event) => {
    event.preventDefault();
    try {
      // snd data to the body of this url
      const res = await fetch('http://localhost:3000/api/world', {
        method: "POST",
        headers: {"content-type":"application/json"},
        // convert obj to json
        body: JSON.stringify( {form: this.state.form} )
      })
      const serverResponse = await res.json();
      console.log(serverResponse)
      this.setState({serverResponse: serverResponse.message})
    } catch (e) {
        console.log(e);
    };
  }

  render () {
    return (
      <div className="App">
        <header className="App-header">
          <h1>{this.state.message}</h1>
          <form onSubmit={this.handelSumit}>
            <input type="text" name="formInput" onChange={this.handelChange} />
            <button type="submit">Submit</button>
            <p>{this.state.serverResponse}</p>
          </form>
        </header>
      </div>
    )
  }
};


export default App;
