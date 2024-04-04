$(document).ready(function () {
  $('INPUT#btn_translate').on('click', start);
  $('INPUT#language_code').on('keypress', (event) => { if (event.which === 13) { start(); } });
});

function start () {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').text(data.hello);
  });
}
