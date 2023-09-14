#!/usr/bin/node

let count = 0; // Initialize a counter variable

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the counter for the next call
};
