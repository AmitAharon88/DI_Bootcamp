// Part I:
const { largeNumber, currentDate } = require('./main.js');
const b = 5;

console.log(largeNumber + b);

// Part II: --> to do tomorrow when we learn http
// const http = require('http');

// const server = http.createServer((request, response) => {
//     console.log('Im Listening');
//     response.setHeader('content-Type', 'text/html');
//     const content = `<p>My module is ${largeNumber + b}</p><h1>Hi there at the frontend</h1>`;
//     response.end(content);
// });
// server.listen(3000);


// Part III: --> to do tomorrow when we learn http

const http = require('http');

const server2 = http.createServer((request, response) => {
    response.setHeader('content-Type', 'text/html');
    const content = `<p>The date and time currently: ${currentDate}</h1>`;
    response.end(content);
});
server2.listen(8080);