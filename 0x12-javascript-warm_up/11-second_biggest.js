#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 2) {
  console.log(0);
} else {
  const nums = [];
  for (let index = 2; index < process.argv.length; index++) {
    nums.push(process.argv[index]);    
  }
  const big = nums.sort();
  console.log(big[0]);
}
