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
  getCharacter(characters, 0);

  function getCharacter (characters, i) {
    if (!characters[i]) { return; }
    request(characters[i], (errChar, responseChar, bodyChar) => {
      if (err) { console.error(errChar); }
      const charJson = JSON.parse(bodyChar);
      console.log(charJson.name);
      getCharacter(characters, i + 1);
    });
  }
});
