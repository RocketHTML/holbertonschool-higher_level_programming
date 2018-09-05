#!/usr/bin/node
let fs = require('fs');
let outfile = process.argv[4];
let file1 = fs.readFileSync(process.argv[2], 'utf-8');
let file2 = fs.readFileSync(process.argv[3], 'utf-8');
let output = file1 + file2;
fs.writeFileSync(outfile, output);
