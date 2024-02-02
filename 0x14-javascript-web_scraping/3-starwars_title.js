#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url) {
  request.get(url, function (err, response, body) {
    if (err) {
        console.log(err);
    } else {
	const film = JSON.parse(body);
	console.log(film.title);
    }
  });
}
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
get(url);
