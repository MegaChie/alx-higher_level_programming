#!/usr/bin/node
const oldList = require('./100-data.js').list;
console.log(oldList);
console.log(oldList.map((x, y) => x * y));
