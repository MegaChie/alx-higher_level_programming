#!/usr/bin/node
// comment text
function factorial (x) {
  if (isNaN(x) || x <= 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const pass = Number(process.argv[2]);
console.log(factorial(pass));
