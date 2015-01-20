$(document).ready(function() {
    $(document).ajaxComplete(redirectAJAXHandler);

    var menu = $('.navbar');
    var origOffsetY = menu.offset().top;
    function scroll() {
        if ($(window).scrollTop() >= origOffsetY) {
            $('.navbar').addClass('navbar-fixed-top');
            $('.content').addClass('menu-padding');
        } else {
            $('.navbar').removeClass('navbar-fixed-top');
            $('.content').removeClass('menu-padding');
        }
    }
    document.onscroll = scroll;
});

$.namespace = function() {
    var a=arguments, o=null, i, j, d;
    for (i=0; i<a.length; i=i+1) {
        d=a[i].split(".");
        o=window;
        for (j=0; j<d.length; j=j+1) {
            o[d[j]]=o[d[j]] || {};
            o=o[d[j]];
        }
    }
    return o;
};



$.namespace("food_week.settings");
food_week.settings.ajaxRedirectEnabled = false;

function redirectAJAXHandler(e, xhr, settings) {
    if (xhr.status == 278) {
        if (food_week.settings.ajaxRedirectEnabled) {
            document.location.href =
                xhr.getResponseHeader("Location").replace(/\?.*$/,
                    "?next=" + window.location.pathname);
        }
    }
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function ajaxPrep(token) {
    console.log("Prepping for CSRF Insert");
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            console.log("Inserting CSRF Token");
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", token);
            }
        }
    });
}