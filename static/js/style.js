$(document).ready(function() {

  $("#user-info").on("submit", function() {
        event.preventDefault();        

        var url = $("#youtube-url").val();        
        
        if(url.search("youtube") >= 1){
            if(url.search('embed') === -1){
                url = "https://www.youtube.com/embed/" + url.split("watch?v=")[1];
            }
        }        

        $("#embedded-video").attr("src", url);        
  });

});
