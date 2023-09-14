#!/usr/bin/node

const size = parseInt(process.argv[2]); // Get the size argument and convert it to an integer

if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}