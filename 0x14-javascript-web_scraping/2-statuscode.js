#!/usr/bin/node
const link = process.argv[2]
request(link, function(error, response, body) {
  console.log(response.statusCode);
});
