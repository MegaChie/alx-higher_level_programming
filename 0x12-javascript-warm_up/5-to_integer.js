#!/usr/bin/node
// comment text
let holder = process.argv[2];
if (typeof(holder) == 'number') {
  console.log(holder);
} else {
  console.log('Not a number');
}
