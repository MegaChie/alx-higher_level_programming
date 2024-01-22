#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i--) {
      const info = data;
      fs.get(info[i], function (error, polo1, body1) {
        if (error) throw error;
        else console.log(JSON.parse(body1).name);
      });
    }
  }
});
