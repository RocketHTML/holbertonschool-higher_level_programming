#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let films = JSON.parse(body).results;
    let sum = 0;
    for (let film of films) {
      for (let person of film.characters) {
        let x = person.split('/');
        let id = x[x.length - 2];
        if (id === '18') {
          sum += 1;
          break;
        }
      }
    }
    console.log(sum);
  }
});
