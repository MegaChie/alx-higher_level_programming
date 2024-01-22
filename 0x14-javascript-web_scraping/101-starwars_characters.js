#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    console.log(data)
    let i = 0;
    while (i < Date.length){
      fs.get(data[i], function (err, content, bod) {
        if (err) throw err;
        else console.log(JSON.parse(bod).name);
      })
      i++;
    }
    }
  });
