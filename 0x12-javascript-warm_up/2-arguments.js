#!/usr/bin/node

const passedArguments = process.argv;
if (passedArguments.length > 3) {
  console.log('Arguments found');
} else if (passedArguments.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
