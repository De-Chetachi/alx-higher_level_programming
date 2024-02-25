// #!/usr/bin/node
// window.onload =
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
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
      },
      xhrFields: {
        withCredentials: false
      }
    });
  });
});
