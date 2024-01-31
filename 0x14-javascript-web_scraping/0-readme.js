#!/usr/bin/node
// a script that reads and prints the content of a file.

const fs = require('fs').promises;

async function readFile (filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    console.log(content);
  } catch (err) {
    console.log(err);
  }
}
const file = process.argv[2];
readFile(file);
