#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url) {
  request.get(url, function (err, response, body) {
    const obj = JSON.parse(body);
    const people = obj["characters"];
    for (let link of people) {
        request(link, function (error, response, body) {
            console.log(JSON.parse(body)["name"]);
	})
    }
	  //console.log(response);
  });
}
const id = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
get(url);
