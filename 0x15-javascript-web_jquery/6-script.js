// Use jQuery to select the div with id update_header and add a click event handler
$('DIV#update_header').click(function() {
    // Within the click event handler, select the header element and update its text
    $('header').text('New Header!!!');
});
