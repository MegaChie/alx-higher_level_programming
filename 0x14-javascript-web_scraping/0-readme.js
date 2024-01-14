#!/usr/bin/node
const fs = require('fs');
fs.readFile(arguments[0], (err, inputD) => {
  if (err) throw err;
  console.log(inputD, toString());
});
