#!/usr/bin/node
const request = require('request');
const args = process.argv;
const filmUrl = `https://swapi-api.hbtn.io/api/films/${args[2]}`;

request(filmUrl, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const characters = JSON.parse(body).characters;

  characters.forEach(character => {
    request(character, function (error, response, body) {
      if (error) {
        return console.log(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
