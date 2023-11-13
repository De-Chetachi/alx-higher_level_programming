#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */

const argv = (require('process')).argv;
const len = argv.length;
const num = Number(argv[2]);

if (isNaN(num) || len === 3) {
  console.log(0);
} else {
  const numa = Number(argv[3]);
  const argvNew = argv.slice(4);
  let max = grt(num, numa);
  let mas = les(num, numa);
  for (const idx in argvNew) {
    const numb = Number(argvNew[idx]);
    mas = grt(mas, numb);
    max = grt(mas, max);
    mas = les(mas, max);
  }
  console.log(mas);
}

function grt (a, b) {
  if (a > b) return a;
  return b;
}
function les (a, b) {
  if (a < b) return a;
  return b;
}
