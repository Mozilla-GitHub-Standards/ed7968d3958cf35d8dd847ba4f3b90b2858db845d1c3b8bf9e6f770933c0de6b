#!/usr/bin/env node

var http = require('http');
var count = 0;

var srv = http.createServer(function (req, res) {
  count += 1
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end(count + "\n");
});

var PORT = parseInt(process.argv[2]) || 9999;

srv.listen(PORT, '127.0.0.1', function() {
    console.log("Server running on port: " + PORT);
});
