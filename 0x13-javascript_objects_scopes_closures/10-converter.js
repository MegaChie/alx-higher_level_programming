#!/usr/bin/node
// comment text
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
