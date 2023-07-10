const express = require('express');
const app = express();

// need to attach the html to the server
app.use('/pic',express.static(__dirname+'/public/picture.html'));
app.use('/form',express.static(__dirname+'/public/form.html'));

// need to create
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
// const bodyParser = require('body-parser');
// app.use(bodyParser.urlencoded({ extended: false }));

app.listen(3000, () => { // runs server on 3000
    console.log('run on 3000 using express');
});

// Route: /aboutMe/:hobby
app.get('/aboutMe/:hobby', (req, res) => {
    const hobby = req.params.hobby; // get an array
    if(typeof hobby !== 'string') {
        return res.status(404).json({msg: 'product not found'});
    }
    res.send(hobby);
});

// Route: /pic
app.get("/pic", (req, res) => {
    res.sendFile(__dirname + "/public/picture.html");
});

// Route: /form
app.get("/form", (req, res) => {
    res.sendFile(__dirname + "/public/form.html");
});

// Route: /formData
app.post('/formData', (req, res) => {
    const email = req.body.email;   
    console.log(email); // im getting undefined and same for message
    const message = req.body.message;
    res.send(`${email} sent you a message: "${message}"`);
 });


    