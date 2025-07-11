$(document).ready(function() {
    // Open all links in a new tab
    $('a').attr('target', '_blank');
    
    // Existing functionality
    $("table").fixMe();
    $(".up").click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 2000);
    });
});
