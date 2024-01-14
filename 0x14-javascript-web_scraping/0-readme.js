#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(process.argv[2], (err, inputD) => {
  if (err) throw err;
  console.log(inputD, toString());
});
