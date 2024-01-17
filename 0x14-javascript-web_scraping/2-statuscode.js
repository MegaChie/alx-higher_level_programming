#!/usr/bin/node
request(process.argv[2], function (error, response, body) {
  console.log('code:', response && response.statusCode); 
});
