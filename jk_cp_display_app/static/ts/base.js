function side_bar_up() {
    $("#side_bar_up").css("width", "0");
    $("#side_bar_up").css("visibility", "hidden");
    $("#side_bar_up").css("transition", "all .25s");
}
function side_bar_down() {
    $("#side_bar_up").css("width", "330");
    $("#side_bar_up").css("visibility", "visible");
    $("#side_bar_up").css("transition", "all .25s");
}