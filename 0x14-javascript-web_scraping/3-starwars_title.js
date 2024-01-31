#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url, id) {
  request.get(url, function (err, response, body) {
    const obj = JSON.parse(body);
    const res = obj.results;
    const id_ = id - 1;
    console.log(res[id_].title);
  });
}
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
get(url, id);
