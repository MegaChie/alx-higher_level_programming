#!/usr/bin/node
// comment text
let arr = [0]
if (process.argv.length == 2 || process.argv.length == 3) {
  console.log('0');
} else {
  for (let i = 0, j = 2; i < process.argv.length; i++) {
    arr[i] = process.argv[j];
    j++;
  }
  arr.sort(function(a, b){return a - b});
  console.log(arr.slice(-2));
}
