#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');
const fs = require('fs').promises;

async function get (url, fp) {
  request.get(url, async function (err, response, body) {
   const content = body;
   await fs.writeFile(fp, content, 'utf-8');
  });
}
const url = process.argv[2];
const filePath = process.argv[3];
get(url, filePath);
