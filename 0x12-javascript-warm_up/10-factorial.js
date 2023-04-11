#!/usr/bin/node
// comment text
function factorial (x) {
  if (isNaN(num) || num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const pass = Number(process.argv[2]);
console.log(factorial(pass));
