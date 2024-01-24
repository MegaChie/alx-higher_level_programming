$(document).ready( function() {
  const link = "https://www.fourtonfish.com/hellosalut/?";
  $("INPUT#btn_translate").on("click", function() {
    const lang = {lang: $("INPUT#language_code").val()};
    $.get(link + $.param(lang), function(json) {
      $("DIV#hello").text(json.hello);
    });
  });
});
