#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

const sourceFile1 = args[0];
const sourceFile2 = args[1];
const destinationFile = args[2];

// Read the content of sourceFile1
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}: ${err.message}`);
    process.exit(1);
  }

  // Read the content of sourceFile2
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate the contents of data1 and data2
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destinationFile
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}: ${err.message}`);
        process.exit(1);
      }
      console.log(`Concatenated files ${sourceFile1} and ${sourceFile2} into ${destinationFile}`);
    });
  });
});
