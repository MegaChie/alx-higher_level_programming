#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const value = Object.values(oldDict);
const key = Object.keys(oldDict);
console.log(value);
console.log(key);
