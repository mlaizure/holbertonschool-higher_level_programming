#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const jsonRes = JSON.parse(body);
  const completeTasks = {};

  jsonRes.forEach(task => {
    if (task.completed) {
      if (completeTasks[task.userId]) {
        completeTasks[task.userId] += 1;
      } else {
        completeTasks[task.userId] = 1;
      }
    }
  });
  console.log(completeTasks);
});
