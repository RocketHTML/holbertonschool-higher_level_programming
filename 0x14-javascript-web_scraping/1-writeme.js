#!/usr/bin/node
let fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});