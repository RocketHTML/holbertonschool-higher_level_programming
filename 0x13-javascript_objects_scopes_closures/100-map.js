#!/usr/bin/node
let oldlist = require('./100-data').list;
let newlist = oldlist.map(x => x * oldlist.indexOf(x));
console.log(oldlist);
console.log(newlist);
