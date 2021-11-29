function side_bar_up() {
    
    $(".side_txt").css("display","none")
    $("#side_bar_up").css("width","0")
    $("#side_bar_up").css("z-index","0")

    $("#side_bar_up").css("visibility","hidden")
    $("#side_bar_up").css("transition","all 1.3s")

    
}


function side_bar_down() {

    $("#side_bar_up").css("width","330")
    $("#side_bar_up").css("z-index","20")
    
    $("#side_bar_up").css("visibility","visible")
    $("#side_bar_up").css("transition","all 1.3s")

    setTimeout(function() {
        $(".side_txt").css("display","block") 
      }, 1000);



        
}





