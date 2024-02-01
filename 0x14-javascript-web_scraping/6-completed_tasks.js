#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url) {
  request.get(url, function (err, response, body) {
    const obj = JSON.parse(body);
    const dict = {};
    for (ob of obj) {
      if (ob.completed) {
        dict[ob.userId] = (dict[ob.userId] || 0) + 1;
      }
    }
    console.log(dict);
  });
}
const url = process.argv[2];
get(url);
