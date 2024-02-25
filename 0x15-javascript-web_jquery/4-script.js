#!/usr/bin/node

$('#toggle_header').on('click', function () {
  $('header').toggleClass('red');
  $('header').toggleClass('green');
});
