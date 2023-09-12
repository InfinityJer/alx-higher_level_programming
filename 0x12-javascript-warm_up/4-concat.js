#!/usr/bin/node

const args = process.argv.slice(2); // Extract command line arguments (excluding "node" and the script name)
const arg1 = args[0] || 'undefined'; // Get the first argument or use 'undefined' if it's missing
const arg2 = args[1] || 'undefined'; // Get the second argument or use 'undefined' if it's missing

console.log(arg1 + ' is ' + arg2);
