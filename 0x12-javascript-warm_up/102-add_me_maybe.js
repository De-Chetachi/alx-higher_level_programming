#!/usr/bin/node

/* Write a script that prints “JavaScript is amazing” */
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
