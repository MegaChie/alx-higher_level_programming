#!/usr/bin/node
const base = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2] + '/';
const link = base.concat(ID);
const fs = require('request');
fs.get(link, function (error, polo, body) {
if (error) console.log(error);
console.log(JSON.parse(polo).title);
});
