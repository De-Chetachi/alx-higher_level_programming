#!/usr/bin/node
// chnage color on click

// const $ = require('jquery');
const head = $('header');
$('#red_header').on('click', function (event) {
  head.css('color', '#FF0000');
});
