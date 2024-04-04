document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').on('click', start);
});

function start () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val();
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
