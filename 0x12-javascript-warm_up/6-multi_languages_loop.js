#!/usr/bin/node
/* Write a script that prints “JavaScript is amazing” */
const string = [];
string[0] = 'C is fun';
string[1] = 'Python is cool';
string[2] = 'JavaScript is amazing';
for (const idx in string) {
  console.log(string[idx]);
}
