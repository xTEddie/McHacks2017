$(document).ready(function() {

    function searchVideo(){
        var url = $("#youtube-url").val().trim();

        if(url.length == 0) return;

        if(url.search("youtube") >= 1){
            if(url.search('embed') === -1){
                url = "https://www.youtube.com/embed/" + url.split("watch?v=")[1];
            }
        }        

        $("#embedded-video").attr("src", url);        
    }

    function searchKeyword(){
        var keyword = $("#search-keyword").val().trim();

        if(keyword.length == 0) return;
        console.log(keyword);

        var url = $("#embedded-video").attr("src");
        console.log(url);    

        $.ajax({
            url: "/search_keyword",
            type: "POST",
            data: {
                "url": url,
                "keyword": keyword
            },
            success: function(data){
                // Write logic to render buttons for time
                console.log(data);
            }
        });

    }

    // Search 
    $("#user-info").on("submit", function() {
        event.preventDefault();            
        searchVideo();    
        searchKeyword();        
    });

});

