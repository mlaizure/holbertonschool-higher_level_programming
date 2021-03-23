#!/usr/bin/node
const dict = require('./101-data').dict;
const dict1 = {};
for (const userId in dict) {
  const occurences = dict[userId];
  if (!(occurences in dict1)) {
    dict1[occurences] = [];
  }
  dict1[occurences].push(userId);
}
console.log(dict1);
