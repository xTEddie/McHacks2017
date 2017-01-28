$(document).ready(function() {

  $("#submit-user-info").on("click", function() {

        var bla = $('#youtube-url').val();

        $("#embeded-video").attr("src", bla);

  });

});
