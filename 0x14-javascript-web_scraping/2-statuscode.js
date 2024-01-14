#!/usr/bin/node
const url = process.argv[2];
request(url, function (error, response, body) {
  console.log("statusCode:", response && response.statusCode);
});
