#!/usr/bin/node
const ID = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + ID;
const fs = require('request');
const name = [];
fs.get(link, function (error, polo, body) {
  if (error) throw error;
  else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < date.length; i++) {
      name[i] = data[i]
    }
})
cosole.log(name);
