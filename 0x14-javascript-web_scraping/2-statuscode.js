#!/usr/bin/node
const link = process.argv[2];
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  console.log(polo.status);
});
