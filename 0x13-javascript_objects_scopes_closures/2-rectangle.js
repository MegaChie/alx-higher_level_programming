#!/usr/bin/node
// comment text
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
  }
  }
};
