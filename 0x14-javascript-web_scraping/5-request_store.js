#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  try {
    fs.writeFileSync(args[3], body, 'utf8');
  } catch (err) {
    console.error(err);
  }
});
