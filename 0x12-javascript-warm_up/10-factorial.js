#!/usr/bin/node
function fact (a) {
    return (a * fact(a - 1));
  }
if (isNaN(process.argv[2]) === false) {
  console.log(fact(parseInt(process.argv[2])));
} else {
  console.log('1');
}
