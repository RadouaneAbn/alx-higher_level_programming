#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

let key;

for (key in dict) {
  const newKey = dict[key];
  if (newKey in newDict) {
    newDict[newKey] = newDict[newKey].concat(key);
  } else {
    newDict[newKey] = [key];
  }
}

console.log(newDict);
