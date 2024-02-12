#!/usr/bin/node
function fact (a) {
  if (a > 0) {
    console.log(a * fact(a - 1));
  }  
}
if (isNaN(process.argv[2]) === false) {
  fact(parseInt(process.argv[2]));
} else {
  console.log('1');
}
