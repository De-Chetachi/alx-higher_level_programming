#!/usr/bin/node
// a script that prints all characters of a Star Wars movie.

const request = require('request');

function get (url) {
  request(url, { json: true }, (err, response, obj) => {
    //const obj = JSON.parse(body)
    //const people = obj["characters"];
    for (let i = 0; i < obj.characters.length; i++) {
        request(obj.characters[i], { json: true }, (error, res, bdy) => {
            console.log(bdy.name);
	})
    }
	  //console.log(response);
  });
}
const id = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
get(url);
