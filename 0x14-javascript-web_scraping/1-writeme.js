#!/usr/bin/node
const fs = require('fs');
const loc = process.argv[2];
const txt = process.argv[3];
fs.writeFile(loc, txt, err => {
  if (err) {
    console.error(err);
  }
});