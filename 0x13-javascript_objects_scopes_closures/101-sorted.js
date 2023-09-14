#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

// Iterate through the keys (user ids) in the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if the occurrences is already a key in the sorted dictionary
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }

  // Add the user id to the list of user ids for that occurrences
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
