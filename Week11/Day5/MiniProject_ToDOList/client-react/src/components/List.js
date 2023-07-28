import { useState } from 'react';

const List = () => {
    const [todos, setTodos] = useState([]);
    const [inputValue, setInputValue] =  useState('');

    const changeList = () => {
        setTodos(prevList => ([
            ...prevList, inputValue
        ]))
    };

    const handleChange = (e) => {
        setInputValue(e.target.value);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            // Save the value to the list of todos
            console.log('Value saved:', inputValue);
            changeList()
            setInputValue(''); // Clear the input after saving the value
            e.target.value = "";
        };
    };

    const removeTodo = (index) => {
        // Remove the todo at the specified index
        setTodos((prevList) => prevList.filter((item, i) => i !== index));
        console.log(todos);
      };
    
    return (
        <>
            <ul>
                {
                    todos.map((todo, index) => (
                        <li id="listItem" key={index} onClick={() => removeTodo(index)}>{todo}</li>
                    )
                )}
            </ul>
            <label for="toDoInput">Add a new todo:</label>
            <input id="toDoInput" name="input" onChange={handleChange} onKeyDown={handleKeyDown} />
        </>
    );
};

export default List