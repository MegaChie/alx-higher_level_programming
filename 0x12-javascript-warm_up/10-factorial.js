#!/usr/bin/node
// comment text
function factorial (x) {
  if (isNaN(x) === true || x <= 0) {
    console.log('1');
  } else {
    let temp = x * factorial(x - 1);
    console.log(temp);
  }
}
const pass = Number(process.argv[2]);
factorial(pass);
