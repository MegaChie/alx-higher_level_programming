const base = "https://www.fourtonfish.com/hellosalut/hello/";
const lang = $("INPUT#language_code").val();
const link = base + "?lang=" + lang;
$("INPUT#btn_translate").on("click", function() {
  $.get(link, function(json) {
  $("DIV#hello").text(json.hello);
  });
});
