const fs = require('fs');
const express = require('express');
const app = express();

// middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Register route
app.post('/register', (req, res) => {
    const { firstName, lastName, email, username, password } = req.body;  // Get form data from request body
    const usersData = getUsersData();  // Read the existing users data from JSON file
    const userExists = usersData.find(user => user.username === username || user.password === password);
    if (userExists) {
      res.send('error1'); // Send error message if username or password already exist
    } else {  // Add new user to the data
      usersData.push({ firstName, lastName, email, username, password });
      writeUsersData(usersData); // Write the updated users data to JSON file
      res.send('registered'); // Send success message for registration
    }
  });

// Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;  // Get form data from request body
    const usersData = getUsersData();  // Read the existing users data from JSON file
    const user = usersData.find(user => user.username === username && user.password === password);
    if (user) {
      res.send(`login`); // Send success message for login
    } else {
      res.send('error2'); // Send error message if user is not registered
    }
  });
  
  // Function to read users data from JSON file
  function getUsersData() {
    const usersData = fs.readFile('users.json', 'utf-8', (err, data) => {
        if (err) {
             return console.log(err);
        }
        console.log(data);
    })
    return JSON.parse(usersData);
  }
  
  // Function to write users data to JSON file
function writeUsersData(usersData) {
    fs.writeFile('users.json', JSON.stringify(usersData), 'utf-8', (err) => {
        if (err) return console.log(err);
    });
};
  
  


// start server
app.listen(3000, () => { // runs server on 3001
console.log('run on 3000 using express');
});
