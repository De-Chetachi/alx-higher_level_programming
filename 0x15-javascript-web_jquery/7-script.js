#!/usr/bin/node
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (person) {
    $('DIV#character').text(person.name);
  }
});
