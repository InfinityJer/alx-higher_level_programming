#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  } else if (n === 0) {
    return 1; // Factorial of 0 is 1
  } else {
    return n * factorial(n - 1); // Recursive computation of factorial
  }
}

const num = parseInt(process.argv[2]); // Get the integer argument and convert it to an integer

const result = factorial(num);
console.log(result);
