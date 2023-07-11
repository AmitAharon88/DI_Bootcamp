const fs = require('fs');

// Read synch method
fs.readFile('RightLeft.txt', 'utf-8', (err, data) => {
    if (err) {
        return console.log(err);
    }
    totalSteps(data);
    minusPosition(data);
});

function totalSteps(data) {
    const dataArray = data.split('');
    let position = 0;
    for (let symbol of dataArray) {
        symbol === '>' ? position += 1 : position -= 1;
    };
    if (position > 0) {
        console.log(`${position} steps to the right`);
    } else {
        console.log(`${position} steps to the left`);
    };
};

function minusPosition(data) {
    const dataArray = data.split('');
    let steps = 0;
    let currentPosition = 0;

    for (let symbol of dataArray) {
       symbol === '>' ? currentPosition += 1 : currentPosition -= 1;
       steps++

       if (currentPosition === -1) {
        console.log(`${steps} steps`)
        break
        };
    }; 
};