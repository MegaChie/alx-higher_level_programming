#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    const arr = [];
    for (let i = 0; i < data.length; i++) {
      arr[i] = data[i];
    }
    console.log(arr);
    for (let i = 0; i < arr.length; i++) {
      fs.get(arr[i], function (error, polo, ans) {
        if (!error) console.log(JSON.parse(ans).name);
      });
    }
  }
});
