#!/usr/bin/node
// comment text
exports.converter = function (base) {
  if (process.argv[2] === 16) {
    console.log(parseInt(base, 16));
  } else if (process.argv[2] === 2) {
    console.log(parseInt(base, 2));
  } else if (process.argv[2] === 8) {
    console.log(parseInt(base, 8));
  }
};
