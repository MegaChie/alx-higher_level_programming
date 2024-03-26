#!/usr/bin/node
const base = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
const fs = require('request');
fs.get(base, (error, polo, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
