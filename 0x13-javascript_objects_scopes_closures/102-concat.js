#!/usr/bin/node
const fs = require('fs');
const cont1 = fs.readFileSync(process.argv[2], 'utf-8');
const cont2 = fs.readFileSync(process.argv[3], 'utf-8');
console.log(cont1);
fs.writeFile(process.argv[4], cont1 + cont2);
