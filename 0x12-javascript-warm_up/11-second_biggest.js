#!/usr/bin/node

let list = [];
for (let i = 2; i < process.argv.length; i++) {
  list.push(parseInt(process.argv[i]));
}

if (list.length < 2) {
  console.log(0);
} else {
  secondBiggest(list);
}

function secondBiggest (list) {
  let biggest = 0;
  let second = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] > biggest) {
      biggest = list[i];
    }
  }

  for (let i = 0; i < list.length; i++) {
    if (list[i] !== biggest && list[i] > second) {
      second = list[i];
    }
  }

  console.log(second);
}
