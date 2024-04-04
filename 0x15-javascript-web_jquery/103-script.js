$(document).ready(function () {
  $('INPUT#btn_translate').on('click', start);
  $('INPUT#language_code').on('keypress', start);
});

function start (event) {
  if (!(event.type === 'click' || (event.type === 'keypress' && event.which === 13))) { return; }
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
