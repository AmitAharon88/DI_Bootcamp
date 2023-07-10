const express = require('express');
const app = express();

app.listen(3000, () => { // runs server on 3001
    console.log('run on 3000 using express');
});

app.get('/', (req, res) => {  // gets tacked on to the servers name
    res.send('<h1>This is my HTML tag</h1>');
});
