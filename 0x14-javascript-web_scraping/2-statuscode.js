#!/usr/bin/node
const polo = await fetch(process.argv[2]);
console.log('code: ', polo.status);
console.log(polo);
