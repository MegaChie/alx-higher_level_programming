#!/usr/bin/node
const link = process.argv[2];
const req = require('request');
req(link, (error, response, body) => {
  if (error) throw error;
  console.log('code: ' + response.statusCode);
});
