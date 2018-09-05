#!/usr/bin/node
let fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, text) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(text);
  }
});
