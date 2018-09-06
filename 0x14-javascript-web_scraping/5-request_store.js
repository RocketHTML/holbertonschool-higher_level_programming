#!/usr/bin/node
let request = require('request');
let fs = require('fs');
let url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(process.argv[3], body);
  }
});
