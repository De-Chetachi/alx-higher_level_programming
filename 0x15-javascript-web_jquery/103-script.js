$(document).ready(function () {
  function callback_ () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      // jsonp: 'callback',
      dataType: 'jsonp',
      jsonp: 'callback',
      data: {
        lang: $('INPUT#language_code').val(),
        format: 'json'
      },
      success: function (greet) {
        $('DIV#hello').text(greet.hello);
      }
      // xhrFields: {
      // withCredentials: false
      // }
    });
  }
  $('INPUT#btn_translate').on('click', callback_);
  $('INPUT#language_code').on('keydown', (event) => {
    if (event.key == 'Enter') { callback_(); }
  });
});
