#!/usr/bin/node
// comment text
let arr = [0]
for (let i = 0, j = 2; i < process.argv.length; i++) {
  arr[i] = process.argv[j];
  j++;
}
arr.sort();
console.log(arr.slice(-2));
