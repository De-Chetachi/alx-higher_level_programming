#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('node:process')).argv;
console.log(`${argv[2]} is ${argv[3]}`);
