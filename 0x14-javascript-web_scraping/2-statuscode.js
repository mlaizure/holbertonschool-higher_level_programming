#!/usr/bin/node
const request = require('request');
const args = process.argv;

request.get(args[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
