#!/usr/bin/node

/* Write a script that prints “JavaScript is amazing” */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
