#!/usr/bin/node
// comment text
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('x' * Number(process.argv[2]));
  }
}
