#!/usr/bin/node
const oldDict = require('./101-data.js').oldDict;
const newDict = {};
for (const i in oldDict) {
  if (newDict[oldDict[i]] === undefined) {
    newDict[oldDict[i]] = [];
  }
  newDict[oldDict[i]].push(i);
}
console.log(newDict);
