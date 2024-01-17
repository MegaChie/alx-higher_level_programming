#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body);
    console.log(data);
    for (let i = 0; i < data.length; i++) {
      fs.get(data[i], function (error, polo, ans) {
        if (!error) console.log(JSON.parse(ans).name);
      });
    }
  }
});
