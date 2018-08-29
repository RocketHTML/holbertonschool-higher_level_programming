#!/usr/bin/node
let x = parseInt(process.argv[2]);
let y = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(x, y);
