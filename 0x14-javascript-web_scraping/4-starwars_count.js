#!/usr/bin/node
const ID = process.argv[2];
const fs = require('request');
fs.get(ID, function (error, polo, body) {
  if (error) console.log(error);
  let count = 0;
  data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].characters.length; j++) {
      if (data[i].characters[j].includes('/18/')) {
          count++;
          break;
        }
    }
  }
});
