#!/usr/bin/node

const passedArgs = process.argv;
const size = passedArgs[2];

if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
