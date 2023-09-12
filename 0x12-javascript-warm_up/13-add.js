#!/usr/bin/node

// Define the add function that takes two integers and returns their sum
function add (a, b) {
  return a + b;
}

// Export the add function so that it can be used in other files
module.exports.add = add;
