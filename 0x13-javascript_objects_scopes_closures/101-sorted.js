#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const newDict = {};
for (const place in dict) {
  if (newDict[dict[place]] === undefined) {
    newDict[dict[place]] = [];
  }
  newDict[dict[place]].push(place);
}
console.log(newDict);
