#!/usr/bin/node

const args = process.argv.slice(2); // Extract command line arguments (excluding "node" and the script name)

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.map(Number).sort((a, b) => b - a); // Convert to numbers and sort in descending order
  console.log(sortedArgs[1]);
}
