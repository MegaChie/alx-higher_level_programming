const base = "https://www.fourtonfish.com/hellosalut/hello/";
const lang = $("INPUT#language_code").text;
const link = base + "?lang=" + lang;
$.get(link, function(json) {
  $("DIV#hello").text(json.hello);
});
