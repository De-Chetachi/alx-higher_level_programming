#!/usr/bin/node
// a script that  display the status code of a GET request.

const request = require('request');

async function get (url) {
  request.get(url, function (err, response, body) {
    const obj = JSON.parse(body);
    const res = obj.results;
    const characterId = 18;
    let charNum = 0;
    // console.log(res);
    for (let i = 0; i < res.length - 1; i++) {
      char_lists = res[i].characters;
	    for (let j = 0; j < char_lists.length - 1; j++) {
	        const newa = char_lists[j].slice(-4);
        if (newa === '/18/') {
		    charNum += 1;
        }
	    }
    }
    console.log(charNum);
  });
}
const url = 'https://swapi-api.alx-tools.com/api/films/';
get(url);
