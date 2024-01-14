#!/usr/bin/node
const request = require('request');
const requestSettings = {
  url: process.argv[2]
};
request (requestSettings, function(error, response, body) {
  console.log(response.statusCode);
});
