// Exercise 1

const express = require('express');
const app = express();
const cors = require('cors');

// not sure if i need this
// app.use('/users',express.static(__dirname+'/public'))


app.listen(3000, () => { // runs server on 3000
    console.log('run on 3000 using express');
});

app.use(cors());

app.use("/", express.static(__dirname + "/public"));

app.get("/user", (req, res) => {
  res.sendFile(__dirname + "/public/index2.html");
});

app.get('/users', (req, res) => {
    const user = {firstname: 'John',lastname: 'Doe'}
    res.send(JSON.stringify(user));
});


// Exercise 2

app.get('/test/:id', (req, res) => {
    console.log(req.params);
    res.json(req.params);
});
    