const http = require('http');


const server = http.createServer((request, response) => {
    response.setHeader('content-Type', 'text/html');
    response.end('<h1>First line</h1><p>Second Line</p><p>Third line</p>');
});


server.listen(3000);