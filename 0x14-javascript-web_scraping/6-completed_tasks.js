#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let todos = JSON.parse(body);
    let results = {};
    for (let todo of todos) {
      let id = todo.userId;
      let complete = todo.completed;
      if (complete) {
        if (results[id] === undefined) {
          results[id] = 0;
        }
        results[id] += 1;
      }
    }
    console.log(results);
  }
});
