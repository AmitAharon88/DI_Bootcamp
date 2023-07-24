import { useState } from 'react';

const Forms = () => {
    // State to manage the username variable
    const [username, setUsername] = useState("");
    const [header, setHeader] = useState("");
    const [age, setAge] = useState(null);
    const [errorMessage, setErrorMessage] = useState("");
    const [textArea, setTextArea] = useState("The content of a textarea goes in the value attribute.");
    const [car, setCar] = useState("Volvo");

    // Function to handle the onChange event and update the username state
    const handelUsernameChange = (event) => {
        const inputUsername = event.target.value;
        setUsername(inputUsername);

        // Update the header variable only if there is a username input
        // inputUsername  ? setHeader(`Hello ${inputUsername}`) : setHeader("");

        // Update header if boht username and age is added
        setHeader(inputUsername !== "" && age !== null ? `Hello ${inputUsername} ${age}` : "");
    };

    const handelAgeChange = (event) => {
        const inputAge = event.target.value;
        setAge(inputAge);

        // Validation with alert
        if (inputAge === "" || isNaN(inputAge)) {
            alert("Your age must be a number");
        };

        // Validation with errorMessage
        if (inputAge === "" || isNaN(inputAge)) {
            setErrorMessage("Your age must be a number");
        };

        // Update header if boht username and age is added
        setHeader(username !== "" && inputAge !== null ? `Hello ${username} ${inputAge}` : "");
    };

    const handleCarChange = (event) => {
        setCar(event.target.value);
    };

    // Function to handle form submission
    const mySubmitHandler = (event) => {
        event.preventDefault();
        alert(`You are submitting ${username}`)
    };

    return (
        <>
            {/* <h2>Hello {username}</h2> */}
            {/* header ony renders when input is provided */}
            <h2>{header}</h2>
            {/* onSubmit goes on form not button */}
            <form onSubmit={mySubmitHandler}>
                <label for="name">Enter your name:</label><br/>
                <input id="name" type="text" name="name" onChange={handelUsernameChange} placeholder="name here" /><br/>
                <label for="name">Enter your age:</label><br/>
                <input type="text" name="age" placeholder="age here" onChange={handelAgeChange} />
                <p><b>{errorMessage}</b></p>
                <br/>
                <button type="submit">Submit</button><br/>
                <textarea value={textArea} rows={6} cols={50}></textarea><br/>
                <select value={car} onChange={handleCarChange}>
                    <option value="Volvo">Volvo</option>
                    <option value="BMW">BMW</option>
                    <option value="Mercedes">Mercedes</option>
                    <option value="Audi">Audi</option>
                </select>
            </form>
        </>
    );
};

export default Forms