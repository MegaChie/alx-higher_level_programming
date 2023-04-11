#!/usr/bin/node
// comment text
function factorial (x) {
  if (x == 0) {
        console.log('1');
    }
    else {
        console.log(x * factorial(x - 1));
    }
}
let pass = Number(process.argv[2]);
factorial(pass);
