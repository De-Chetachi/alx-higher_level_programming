#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;
const num = Number(argv[2]);

function fact (a) {
  if (isNaN(num)) return 1;
  if (a === 1) return 1;
  return (a * fact(a - 1));
}

console.log(fact(num));
