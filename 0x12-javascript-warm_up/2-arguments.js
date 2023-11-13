#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;
const num = argv.length;
if (num === 2) {
  console.log('No argument');
} else if (num === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
