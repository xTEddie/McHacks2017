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

        var results = $("#results");
        results.html(""); // Delete content in table
        
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

                var data_size = Object.keys(data).length;                

                var output = "";
                
                $.each(data, function(index, value){   
                    var key = Object.keys(value)[0];                                     
                    output += "<button type='button' class='btn btn-danger timestamp' value='" + value[key] + "'>" + '<i class="fa fa-play" aria-hidden="true"></i>&nbsp' +  '<span style="color:black;">' + key + "</span>" + "</button>&nbsp";
                    
                    if((parseInt(index) + 1) % 5 == 0){
                        output += "<br>";
                    }
                });

                results.html(output);

                $(".timestamp").click(function(){      
                    var value = $(this).attr("value");                                                  
                    var new_url = url + "?start=" + parseInt(value);
                    $("#embedded-video").attr("src", new_url);
                });
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

