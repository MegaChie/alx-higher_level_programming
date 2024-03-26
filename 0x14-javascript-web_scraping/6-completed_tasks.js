#!/usr/bin/node
const ID = process.argv[2];
const fs = require('request');
fs.get(ID, function (error, polo, body) {
  if (error) throw error;
  else {
    const done = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (!(data[i].userId in done)) done[data[i].userId] = 1;
        else done[data[i].userId] += 1;
      }
    }
    console.log(done);
  }
});
