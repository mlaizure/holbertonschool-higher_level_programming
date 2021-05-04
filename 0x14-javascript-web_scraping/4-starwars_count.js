#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let num = 0;
  const jsonRes = JSON.parse(body).results;

  jsonRes.forEach(episode => {
    episode.characters.forEach(character => {
      if (character.includes('18')) {
        num++;
      }
    });
  });
  console.log(num);
});
