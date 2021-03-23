#!/usr/bin/node
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const dest = process.argv[4];
const file1Content = fs.readFileSync(file1, 'utf8');
const file2Content = fs.readFileSync(file2, 'utf8');
const destContent = file1Content + file2Content;
fs.writeFileSync(dest, destContent);
