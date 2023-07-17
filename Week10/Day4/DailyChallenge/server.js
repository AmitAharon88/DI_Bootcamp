import express from 'express';
import path from 'path';
import {promises as fsPromises} from "fs" ;
const app = express();
const __dirname = path.resolve(); //create dirname

//needed for put and post methods
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// we need this line to make the files in public folder available
app.use(express.static(__dirname + "/public"));

// for resgister
app.get("/registeruser", (req, res) => {
    res.sendFile(__dirname + "/public/register.html")
})

app.post("/registeruser", async (req, res) => {
    const dataBody = req.body;
    const readFileResponse = await readuser(dataBody);
    res.json(readFileResponse);
})


async function readuser (currentUser) {
    console.log("in readuser");
    
    const data = await fsPromises.readFile(__dirname + "/public/data.json")
    .catch((err) => console.error('Failed to read file', err));
    
    const datausers = JSON.parse(data); //array of objects

    console.log("datausers", datausers);
    
    const findUser = datausers.findIndex((element) => 
            element.username === currentUser.username)

    console.log("findUser", findUser);

    if (findUser >= 0) {
        console.log("Username already exists");
        return "User already exists";
    } else {
        datausers.push(currentUser);
        console.log("User added successfully", datausers);
        //VERY IMPORTANT TO STRINGIFY THE DATA SENT TO WRITE FILES
        await fsPromises.writeFile(__dirname + "/public/data.json", JSON.stringify(datausers));
        return "Hello, Your account has been created";
    }
}

// for login
// renters the page
app.get("/loginuser", (req, res) => {
  res.sendFile(__dirname + "/public/login.html")
})

// sends input and checks it
app.post("/loginuser", async (req, res) => {
// login input
  const dataBody = req.body;
  const readLoginResponse = await loginUser(dataBody);
  res.json(readLoginResponse);
})

async function loginUser (currentUser) { 
  const data = await fsPromises.readFile(__dirname + "/public/data.json")
  .catch((err) => console.error('Failed to read file', err));

// data from json- all those who registered
  const datausers = JSON.parse(data); //array of objects
// loops over all the users in the json file and checks the user username/password and compares it that of the person who is trying to login
  const foundUserLogin = datausers.find((user) => user.username === currentUser.username && user.password === currentUser.password);

  if (foundUserLogin) {
    return `Hi ${user.firstName}, welcome back!`;
  } else {
    return 'Username is not registered';
  }
};

app.listen("3000", () => {
    console.log("SERVER LISTENING");
});
