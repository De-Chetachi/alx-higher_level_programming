#!/usr/bin/node
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: function (greet) {
    $('DIV#hello').text(greet.hello);
  }
});
