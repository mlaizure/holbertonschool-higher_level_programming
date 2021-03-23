#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list1 = list.map((value, idx) => value * idx);
console.log(list1);
