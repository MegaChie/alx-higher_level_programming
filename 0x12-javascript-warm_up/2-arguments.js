#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log(process.argv[2]);
} else {
  console.log('Arguments found');
}
