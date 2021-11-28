function side_bar_up() {
    $("#side_bar_up").css("display","none")
    $("#side_bar_down").css("display","block")
    
    
}


function side_bar_down() {
    $("#side_bar_up").css("display","block")
    $("#side_bar_down").css("display","none")
    
    
}

$(function(){
    if ($("#all").css("width","1500px") > window.innerHeight){
        $("#side_bar_up").css("display","none")
        $("#side_bar_down").css("display","block")
    }
});


