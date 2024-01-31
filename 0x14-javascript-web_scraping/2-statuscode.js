#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url) {
  request.get(url, function (err, response, body) {
    const code = response.statusCode;
    console.log(`code: ${code}`);
  });
}
const url = process.argv[2];
get(url);
