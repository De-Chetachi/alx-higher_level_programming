#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;
const len = argv.length;
const num = Number(argv[2]);

if (isNaN(num) || len === 3) {
  console.log('0');
} else {
  const argvNew = argv.slice(3);
  let max = num;
  for (const idx in argvNew) {
    const numa = Number(argvNew[idx]);
    if (numa > num) max = numa;
  }
  console.log(max);
}
