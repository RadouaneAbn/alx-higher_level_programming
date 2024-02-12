#!/usr/bin/node

const myArgs = process.argv;
const numberList = myArgs.filter(n => !isNaN(n)).map(Number);

if (myArgs.length < 4) {
  console.log(0);
} else {
  numberList.sort(function (a, b) { return b - a; });
  console.log(numberList[1]);
}
