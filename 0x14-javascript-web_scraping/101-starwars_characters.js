#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    let i = 0;
    start:
    fs.get(data[i], function (error1, polo1, body1) {
      if (error1) throw error1;
      else console.log(JSON.parse(body1).name);
      i++;
      if (i < data.length) goto start;
    });
  });
