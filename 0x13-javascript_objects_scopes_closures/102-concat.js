#!/usr/bin/node
const fs = require('fs');
const cont1 = fs.readFile(process.argv[2], 'utf-8');
const cont2 = fs.readFile(process.argv[3], 'utf-8');
fs.writeFile(process.argv[4], a + b);
