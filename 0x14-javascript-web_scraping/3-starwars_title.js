#!/usr/bin/node
let request = require('request');
let url = `https://swapi.co/api/films/${process.argv[2]}/`;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    console.log(data.title);
  }
});
