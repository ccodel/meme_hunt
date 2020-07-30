$(document).ready(function() {
  setTimeout(function() {
    $(".alert").alert('close');
  }, 4000);
});

/*
$(document).ready(function() {
  setTimeout(function() {
    $(".alert").fadeTo(2000, 500).slideUp(200, function() {
      $(".alert").alert('close');
    });
  }, 2000);
});
*/
