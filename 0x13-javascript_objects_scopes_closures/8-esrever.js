#!/usr/bin/node
// comment text
exports.esrever = function (list) {
  const used = [];
  for (let i = list.length - 1; i >= 0; i--) {
    used.push(list[i]);
  }
  return used;
};