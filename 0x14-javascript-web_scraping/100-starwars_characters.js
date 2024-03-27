#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const bodyJson = JSON.parse(body);
  const characters = bodyJson.characters;

  for (let i = 1; i <= characters.length; i++) {
    const charUrl = 'https://swapi-api.alx-tools.com/api/people/' + i;
    request(charUrl, (err, response, bodyChar) => {
      if (err) {
        console.error(err);
      } else {
        const charJson = JSON.parse(bodyChar);
        if (charJson.name) { console.log(charJson.name); }
      }
    });
  }
});
