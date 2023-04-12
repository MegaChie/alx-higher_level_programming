#!/usr/bin/node
// comment text
let n = 0;
exports.converter = function (base) {
  if (process.argv[2] === 16) {
    parseInt(base, 16);
  } else if (process.argv[2] === 2) {
    parseInt(base, 2);
  } else if (process.argv[2] === 8) {
    parseInt(base, 8);
  }
};
