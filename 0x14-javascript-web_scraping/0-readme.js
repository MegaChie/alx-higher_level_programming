#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(process.argv[0], (err, inputD) => {
  if (err) throw err;
  console.log(inputD, toString());
});
