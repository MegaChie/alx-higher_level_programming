#!/usr/bin/node
// comment text
function factorial (x) {
  if (isNaN(x) === true || x <= 0) {
    console.log('1');
  } else {
    console.log(x * factorial(x - 1));
  }
}
const pass = Number(process.argv[2]);
factorial(pass);
