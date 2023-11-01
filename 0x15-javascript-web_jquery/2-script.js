// Use jQuery to select the div with id red_header and add a click event handler
$('DIV#red_header').click(function() {
    // Within the click event handler, select the header element and update its text color to red
    $('header').css('color', '#FF0000');
});
