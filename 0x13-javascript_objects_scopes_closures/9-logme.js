#!/usr/bin/node
exports.logMe = function (item) {
  if (this.log === undefined) {
    this.log = 0;
  }
  console.log(`${this.log}: ${item}`);
  this.log += 1;
};
