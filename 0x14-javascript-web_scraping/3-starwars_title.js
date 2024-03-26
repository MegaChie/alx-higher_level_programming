#!/usr/bin/node
const base = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2] + '/';
const link = base.concat(ID);
const fs = require('request');
fs.get(link, (error, polo, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
