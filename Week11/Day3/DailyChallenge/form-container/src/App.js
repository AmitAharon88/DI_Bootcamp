import { useState } from 'react';
import FormComponent from "./components/FormComponent.js"
import './App.css';

function App() {
  const [formInputs, setFormInputs] = useState({});
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);

  const handelChange = (e) => {
    const name = e.target.name;
    const value = e.target.type === "checkbox" ? e.target.checked: e.target.value;
    setFormInputs({...formInputs, [name]: value});
  };

  const handelSubmit = async (e) => {
    e.preventDefault();
    console.log(formInputs);

    setIsFormSubmitted(true);

    // generate a URL query
    const query = new URLSearchParams(formInputs).toString();
    console.log("query=>", query);

    // Updating the URL with the query parameters
    window.history.pushState(null, '', `/?${query}`);

  };

  return (
    <div className="App">
      <h1>Sample form</h1>
        <form onSubmit={(e) => handelSubmit(e)} method="POST">
          <input name="firstName" placeholder="First Name" onChange={(e)=>handelChange(e)}/><br/>
          <input name="lastName" placeholder="Last Name" onChange={(e)=>handelChange(e)}/><br/>
          <input name="age" placeholder="Age" onChange={(e)=>handelChange(e)}/><br/>
          <label>Select your destination</label><br/>
          <select name="destination" onChange={(e)=> handelChange(e)}>
              <option>Thailand</option>
              <option>Japan</option>
              <option>Brazil</option>
          </select><br/>
          <label>Dietary restrictions</label><br/>
          <label for="nutsFree">Nuts free</label><br/>
          <input id="nutsFree" type="checkbox" name="nutsFree" onChange={(e) => handelChange(e)} /><br/>
          <label for="lacFree">Lactose free</label><br/>
          <input id="lacFree" type="checkbox" name="lacFree" onChange={(e) => handelChange(e)} /><br/>
          <label for="veganFree">Vegan free</label><br/>
          <input id="veganFree" type="checkbox" name="veganFree" onChange={(e) => handelChange(e)} /><br/>
          <button type="submit">Submit</button>
        </form>
        <hr/>
        {/* only shows FormComponent if submitted */}
        {isFormSubmitted && <FormComponent formInputs={formInputs} />}
        {/* shows FormComponent as your filling in the form */}
        {/* <FormComponent formInputs={formInputs} /> */}
    </div>
  );
}

export default App;
