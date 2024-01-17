#!/usr/bin/node
const link = process.argv[2]
request(link, function(error, response, body) {
  if (error) throw error;
  console.log(response.statusCode);
});
