#!/usr/bin/node

const args = process.argv.slice(2); // Extract command line arguments (excluding "node" and the script name)
const firstArg = args[0];

if (!isNaN(firstArg) && Number.isInteger(Number(firstArg))) {
  console.log('My number:', parseInt(firstArg));
} else {
  console.log('Not a number');
}
