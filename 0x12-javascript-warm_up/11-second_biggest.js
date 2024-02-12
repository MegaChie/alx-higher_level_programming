#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const nums = [];
  for (let index = 2; index < process.argv.length; index++) {
    nums.push(process.argv[index]);
  }
  const big = nums.sort(function (a, b) { return a - b; });
  console.log(big[big.length - 2]);
}
