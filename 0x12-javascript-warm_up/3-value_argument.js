#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
