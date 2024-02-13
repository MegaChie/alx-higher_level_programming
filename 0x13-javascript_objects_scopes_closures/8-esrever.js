#!/usr/bin/node
exports.esrever = function (list) {
  const reveList = [];
  for (let index = list.length - 1; index > 0; index--) {
    reveList.push(list[index]);
  }
  return reveList;
};
