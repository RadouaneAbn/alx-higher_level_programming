#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i; const j = list.length;

  for (i = 0; i < j; i++) {
    newList[i] = list[j - i - 1];
  }

  return (newList);
};
