var http = require('http');

var x = 0;

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  x = x + 1;
  res.end(x + "");
}).listen(8000);
