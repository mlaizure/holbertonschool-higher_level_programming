#!/usr/bin/node
const OrigSquare = require('./5-square.js');
module.exports = class Square extends OrigSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; ++i) {
      console.log(c.repeat(this.width));
    }
  }
};
