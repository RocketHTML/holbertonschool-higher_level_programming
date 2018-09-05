#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let sum = 0;
  for (let ele of list) {
    if (ele === searchElement) {
      sum += 1;
    }
  }
  return sum;
};
