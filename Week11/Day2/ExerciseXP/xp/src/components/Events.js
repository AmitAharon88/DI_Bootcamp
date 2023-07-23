import { useState } from 'react';

const clickMe = () => {
    alert('I was clicked');
};

const handleKeyDown = (event) => {
    if (event.key === "Enter") {
        alert(`The Enter key was pressed, your input is: ${event.target.value}`);
    };
};

const Events = () => {
    const [isToggleOn, setIsToggleOn] = useState(true)

    const toggleHandeler = () => {
        setIsToggleOn((prevIsToggleOn) => !prevIsToggleOn);
    };
    
    return (
        <>
            <button onClick={clickMe}>Click Me</button>
            <input onKeyDown={handleKeyDown} placeholder="Press they ENTER key!"></input>
            <button onClick={toggleHandeler}>{isToggleOn ? "ON" : "OFF"}</button>
        </>
    )
}

export default Events