#!/usr/bin/node

const request = require('request');

const characterId = '18';
const url = process.argv[2];
const pattern = /\/(\d+)\/$/;
let moviesCount = 0;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  const bodyJson = JSON.parse(body);
  const moviesList = bodyJson.results;

  for (let i = 0; i < moviesList.length; i++) {
    const movie = moviesList[i];
    const characters = movie.characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].match(pattern)[1] === characterId) {
        moviesCount++;
      }
    }
  }

  console.log(moviesCount);
});
