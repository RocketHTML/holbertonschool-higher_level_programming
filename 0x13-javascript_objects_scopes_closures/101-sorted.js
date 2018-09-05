#!/usr/bin/node
let occurrences = require('./101-data').dict;
let transformed = {};
for (let key in occurrences) {
  let value = occurrences[key];

  if (transformed[value] === undefined) {
    transformed[value] = [];
  }

  transformed[value].push(key);
}
console.log(transformed);
