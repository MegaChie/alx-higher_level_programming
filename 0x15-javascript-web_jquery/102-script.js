$(document).ready( function() {
  const link = "https://www.fourtonfish.com/hellosalut/hello/";
  $("INPUT#btn_translate").on("click", function() {
    $.get(link, + $.param({ lang: $('INPUT#language_code').val() }), function(json) {
      $("DIV#hello").html(json.hello);
    });
  });
});
