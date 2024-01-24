$("document").ready(function() {
  $("INPUT#btn_translate").on("click", function {
    const base = "https://www.fourtonfish.com/hellosalut/";
    const lang = $("INPUT#language_code").val();
    const link = base + "?lang=" + lang;
    $.get(link, function(json) {
      $("DIV#hello").text(json.hello);
    });
  });
});
