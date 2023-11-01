// Use jQuery to select the div with id red_header and add a click event handler
$('DIV#red_header').click(function() {
    // Within the click event handler, select the header element and add the class red
    $('header').addClass('red');
});
