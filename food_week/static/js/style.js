
window.onload = function() {
    var speed = 300;
    $(".btn-tooltip").hover(function () {
        $(this).transition({
            width: 'auto'
        }, speed, 'in-out');
    }, function () {
        $(this).transition({
            width: 24
        }, speed, 'in-out');
    });
};