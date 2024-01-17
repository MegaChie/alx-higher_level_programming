#!/usr/bin/node
const ID = process.argv[2];
const opener = require('request');
opener.get(ID, function (error, polo, body) {
  if (error) throw error;
  else {
    const writer = require('fs');
    const loc = process.argv[3];
    writer.writeFile(loc, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
