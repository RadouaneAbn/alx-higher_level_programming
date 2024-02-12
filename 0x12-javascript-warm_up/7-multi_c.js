#!/usr/bin/node

const passedArgs = process.argv;
if (passedArgs.length < 3) {
  console.log('Missing number of occurrences');
}

const n = Number(passedArgs[2]);
let i = 0;

while (i < n) {
  console.log('C is fun');
  i++;
}
