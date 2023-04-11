#!/usr/bin/node
// comment text
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else if (Number(process.argv[2]) <= 0) {
  console.log('');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('x'.repeat(Number(process.argv[2])));
  }
}
