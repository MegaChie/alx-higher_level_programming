#!/usr/bin/node
if (process.argv.length === 2 || isNaN(process.argv)) {
  console.log(0);
} else {
  const nums = [];
  for (let index = 2; index < process.argv.length; index++) {
    nums[index - 2] = process.argv[index];    
  }
  console.log(nums.sort()[1])
}
