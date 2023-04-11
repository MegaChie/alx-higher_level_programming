#!/usr/bin/node
// comment text
function factorial (x) {
  if (x == 0) {
        return 1;
    }
    else {
        return x * factorial(x - 1);
    }
}
let pass = Number(process.argv[2]);
factorial(pass);
