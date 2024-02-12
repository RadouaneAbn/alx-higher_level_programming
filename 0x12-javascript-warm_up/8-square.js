#!/usr/bin/node

const passedArgs = process.argv;
const size = passedArgs[2];

if (isNaN(size)) {
  console.log('Missing size');
}

let i, j;

for (i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
