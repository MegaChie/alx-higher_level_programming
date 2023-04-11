#!/usr/bin/node
// comment text
let arr = [0]
function sortNumber (a, b) {
  return a - b;
}
if (process.argv.length == 2 || process.argv.length == 3) {
  console.log('0');
} else {
  for (let i = 2; i < argsLen; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort(sortNumber);
  console.log(arr.slice(-2));
}
