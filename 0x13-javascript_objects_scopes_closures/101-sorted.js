#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const newDict = {};
const key = Object.keys(oldDict)
for (let index = 0; index < key.length; index++) {
  if (newDict[oldDict[key[index]]].push(key[index]) === undefined) {
    newDict[oldDict[key[index]]] = [];
  }
  newDict[oldDict[key[index]]].push(key[index]);
}
console.log(newDict);
