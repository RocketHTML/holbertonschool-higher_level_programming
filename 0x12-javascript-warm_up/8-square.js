#!/usr/bin/node
input = parseInt(process.argv[2]);
if (isNaN(input)) { console.log('Missing size'); }
else {
  str = '';
  for (let i = 0; i < input; i++) { str += 'x'; }
  str += '\n';
  str = str.repeat(input)
  str = str.substring(0, str.length - 1);
  console.log(str);
}
