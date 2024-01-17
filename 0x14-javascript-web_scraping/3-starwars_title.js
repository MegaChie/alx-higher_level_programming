#!/usr/bin/node
const base = "https://swapi-api.alx-tools.com/api/films/";
const ID = process.argv[2];
const link = base.concat(ID);
console.log(link);
