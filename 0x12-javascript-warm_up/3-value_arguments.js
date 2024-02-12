#!/usr/bin/node

const passedArgs = process.argv;

if (passedArgs[2] !== undefined) {
  console.log(passedArgs[2]);
} else {
  console.log('No argument');
}
