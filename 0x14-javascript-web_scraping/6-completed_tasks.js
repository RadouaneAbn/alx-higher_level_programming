#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const bodyJson = JSON.parse(body);
  const result = {};

  for (let i = 0; i < bodyJson.length; i++) {
    const key = String(bodyJson[i].userId);
    if (!bodyJson[i].completed) { continue; }
    if (!result[key]) { result[key] = 0; }
    result[key]++;
  }

  console.log(result);
});
