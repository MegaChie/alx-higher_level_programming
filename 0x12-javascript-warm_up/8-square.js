#!/usr/bin/node
// comment text
const num = Number(process.argv[2]);

if (num) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else if (num < 0) {
  console.log('');
} else {
  console.log('Missing size');
}
