#!/usr/bin/node
const oldDict = require('./101-data.js').oldDict;
const newDict = {};
for (const place in oldDict) {
  if (newDict[oldDict[place]] === undefined) {
    newDict[oldDict[place]] = [];
  }
  newDict[oldDict[place]].push(place);
}
console.log(newDict);
