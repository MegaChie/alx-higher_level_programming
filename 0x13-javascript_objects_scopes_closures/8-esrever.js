#!/usr/bin/node
exports.esrever = function (list) {
  for (let index = list.length - 1; index > 0; index--) {
    const reveList = [];
    reveList.push(list[index]);
  }
  return reveList;
};
