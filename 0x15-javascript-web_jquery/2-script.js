#!/usr/bin/node
// chnage color on click

const $ = require("jquery");
$("#red_header").bind('click', function() {
    $('header').css('color', 'FF0000');
});