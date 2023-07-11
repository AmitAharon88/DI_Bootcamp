const fs = require('fs');


// Read synch method
fs.readFile('text', 'utf-8', (err, data) => {
if (err) {
     return console.log(err);
}
console.log(data);
})

// Write File
const text = 'New file with new text';

fs.writeFile('newText', text, 'utf-8', (err) => {
    if (err) return console.log(err);
});

// Append File
const addText = 'Look at me appending my text'

fs.appendFile('newText', addText, 'utf-8', (err) => {
    if (err) return console.log(err);
});


// Delete a File
fs.unlink('newText', (err) => {
    if(err) return console.log(err);
});
    
    
