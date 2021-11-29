function side_bar_up() {
    $(".side_txt").css("display", "none");
    $("#side_bar_up").css("width", "0");
    $("#side_bar_up").css("z-index", "0");
    $("#side_bar_up").css("visibility", "hidden");
    $("#top").css("padding-left", "65px");
    $("#bottom").css("padding-left", "135px");
    $("#side_bar_up").css("transition", "all 1.3s");
    $("#top").css("transition", "all 1.3s");
    $("#bottom").css("transition", "all 1.3s");
}
function side_bar_down() {
    $("#side_bar_up").css("width", "330");
    $("#side_bar_up").css("z-index", "20");
    $("#top").css("padding-left", "330px");
    $("#top").css("transition", "all 1.3s");
    $("#bottom").css("padding-left", "500px");
    $("#bottom").css("transition", "all 1.3s");
    $("#side_bar_up").css("visibility", "visible");
    $("#side_bar_up").css("transition", "all 1.3s");
    setTimeout(function () {
        $(".side_txt").css("display", "block");
    }, 1000);
}
