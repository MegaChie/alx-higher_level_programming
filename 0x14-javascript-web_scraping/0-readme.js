#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (err, data) {
  if (!err) {
    console.log(data.toString().trim());
  } else console.log(err);
});
