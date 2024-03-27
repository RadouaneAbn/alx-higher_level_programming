#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');

const url = process.argv[2];
const outputFile = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  const writer = fs.createWriteStream(outputFile);
  writer.write(body);
});
