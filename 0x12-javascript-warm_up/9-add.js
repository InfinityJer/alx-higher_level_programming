#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2]); // Get the first integer argument and convert it to an integer
const num2 = parseInt(process.argv[3]); // Get the second integer argument and convert it to an integer

if (!isNaN(num1) && !isNaN(num2)) {
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log('NaN');
}
