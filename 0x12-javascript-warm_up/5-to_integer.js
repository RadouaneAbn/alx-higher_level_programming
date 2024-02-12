#!/usr/bin/node

const passedArgs = process.argv;
const result = Number(passedArgs[2]);

if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + result);
}
