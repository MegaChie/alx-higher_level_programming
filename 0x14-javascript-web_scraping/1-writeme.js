#!/usr/bin/node
const fs = require('fs');
const loc = process.argv[2];
fs.readFile(loc, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
