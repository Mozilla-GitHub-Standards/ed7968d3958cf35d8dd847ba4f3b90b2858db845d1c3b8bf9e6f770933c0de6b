#!/usr/bin/env node

/*
 * this spins up a return 200 for everything web server
 * to make it easier to test the load testing scripts
 *
 * run it like: ./test-server.js
 */

var http = require('http');

var count = 0, dataReceived = 0 ;

var srv = http.createServer(function (req, res) {
  count += 1;

  req.on('data', function(chunk) { 
      dataReceived += chunk.length; 
  });

  req.on('end', function() {
      res.writeHead(200, {'Content-Type': 'text/plain'});
      res.end(count + " reqs, " + dataReceived + " bytes \n");
  });

});

var PORT = parseInt(process.argv[2]) || 9999;

srv.listen(PORT, '127.0.0.1', function() {
    console.log("Server running on port: " + PORT);
});
