#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X'; // Set default character to 'X'
    }

    // Print the square using the specified character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
