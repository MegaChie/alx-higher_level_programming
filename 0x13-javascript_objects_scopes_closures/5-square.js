#!/usr/bin/node
// comment text
module.exports = class Square extends require('./2-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
