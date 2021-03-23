#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const half = Math.floor(len / 2);
  for (let i = 0; i < half; ++i, --len) {
    const tmp = list[i];
    list[i] = list[len - 1];
    list[len - 1] = tmp;
  }
  return list;
};
