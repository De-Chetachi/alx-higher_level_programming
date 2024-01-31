#!/usr/bin/node
// a script that reads and prints the content of a file.

const fs = require('fs').promises;

async function writeFile (filePath, content) {
  try {
    await fs.writeFile(filePath, content);
  } catch (err) {
    console.log(err);
  }
}
const file = process.argv[2];
const content = process.argv[3];
writeFile(file, content);
