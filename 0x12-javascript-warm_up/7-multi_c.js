#!/usr/bin/node
let input = process.argv[2];
if (isNaN(input)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(input); i++) {
    console.log('C is fun');
  }
}
