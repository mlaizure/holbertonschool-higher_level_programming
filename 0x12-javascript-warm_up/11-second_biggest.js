#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let i = 2;
  let j = 0;
  const arr = [];
  while (process.argv[i]) {
    arr[j++] = parseInt(process.argv[i], 10);
    ++i;
  }
  const max = Math.max(...arr);
  arr.splice(arr.indexOf(max), 1);
  console.log(Math.max(...arr));
}
