#!/usr/bin/node
let fs = require('fs');
fs.readFile(process.argv[2], function (err, contents) {
  if (err) throw err;
  console.log(contents, toString().trim());
});
