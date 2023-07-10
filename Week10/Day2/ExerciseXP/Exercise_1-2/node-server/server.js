const http = require('http');

const server = http.createServer((request, response) => {
const user = {
    firstname: 'John',
    lastname: 'Doe'
}
response.setHeader('content-Type', 'application.json');
response.end(JSON.stringify(user));
});

server.listen(8080);