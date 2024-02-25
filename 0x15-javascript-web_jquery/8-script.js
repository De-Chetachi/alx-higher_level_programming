#!/usr/bin/node
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (films) {
    res_s = films.results;
    $.each(res_s, function (i, res) {
      $('UL#list_movies').append(`<li>${res.title}</li>`);
    });
  }
});
