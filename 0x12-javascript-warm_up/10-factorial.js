#!/usr/bin/node

const myArgs = process.argv;
const number = Number(myArgs[2]);

function factorial (n) {
  if (n > 1) {
    return (n * factorial(n - 1));
  } else {
    return (1);
  }
}

console.log(factorial(number));
