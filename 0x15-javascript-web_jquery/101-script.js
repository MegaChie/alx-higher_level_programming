function() {
  if ($("div#add_item").on("click")) {
    function() {
    $("UL.my_list").append("<li>Item</li>")
  });
  }
  if ($("DIV#remove_item").on("click")) {
    function() {
    $("UL.my_list").last().remove("<li>Item</li>");
    });
  }
}
