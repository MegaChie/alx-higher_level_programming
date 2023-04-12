#!/usr/bin/node
// comment text
exports.converter = function (base) {
  if (process.argv[2] == 16) {
    console.log(base.toString(16));
  } else if (process.argv[2] == 2) {
    console.log(base.toString(2));
  } else if (process.argv[2] == 8) {
    console.log(base.toString(8));
  }
};
