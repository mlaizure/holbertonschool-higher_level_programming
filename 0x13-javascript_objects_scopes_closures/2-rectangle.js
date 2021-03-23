#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0) {
      // pass
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
