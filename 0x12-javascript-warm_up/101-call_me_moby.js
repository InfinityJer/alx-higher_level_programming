#!/usr/bin/node

// Define the callMeMoby function that takes x and aFunction as parameters
function callMeMoby (x, aFunction) {
  for (let i = 0; i < x; i++) {
    aFunction();
  }
}

// Export the callMeMoby function so that it can be used in other files
module.exports.callMeMoby = callMeMoby;
