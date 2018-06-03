$("tr").click(function() {
  window.location.href = $(this).data("href");
});