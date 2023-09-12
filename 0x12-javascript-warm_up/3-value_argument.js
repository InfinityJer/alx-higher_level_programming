#!/usr/bin/node

const args = process.argv.slice(2); // Extract command line arguments (excluding "node" and the script name)
const firstArg = args[0]; // Get the first argument from the args array

if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
