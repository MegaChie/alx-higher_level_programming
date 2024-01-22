#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    console.log(data);
    data.shift();
    console.log(data);
    // for (; i !== 0; i--) {
    //   fs.get(data[0], function (error, polo, body) {
    //     if (error) throw error;
    //     else console.log(JSON.parse(body).name);
    //   });
    //   data.shift();
    // }
  }
});
