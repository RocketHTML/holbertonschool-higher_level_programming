#!/usr/bin/node
let oldlist = require('./100-data').list;
let newlist = []
let i = 0;
if (oldlist.length > 0) {
  newlist = oldlist.map(x => x * i++);
}
console.log(oldlist);
console.log(newlist);
