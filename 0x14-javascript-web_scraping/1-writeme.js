#!/usr/bin/node
const fs = require('node:fs/promises');
const loc = process.argv[2];
const txt = process.argv[3];
fs.writeFile(loc, txt, { flag: 'a+'}, err => {
  if (err){
    console.error(err);
  }
});
