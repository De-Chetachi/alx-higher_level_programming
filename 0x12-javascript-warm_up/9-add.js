#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);
function add(a, b) {
  return (a + b);
}
console.log(add(num1, num2));
