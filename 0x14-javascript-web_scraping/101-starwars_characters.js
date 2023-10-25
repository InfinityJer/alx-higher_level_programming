#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    const characterRequests = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    });

    Promise.all(characterRequests)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  }
});
