#!/usr/bin/node

// Define the addMeMaybe function that takes a number and a function as parameters
function addMeMaybe (number, theFunction) {
  number += 1; // Increment the number
  theFunction(number); // Call the provided function with the incremented number as an argument
}

// Export the addMeMaybe function so that it can be used in other files
module.exports.addMeMaybe = addMeMaybe;
