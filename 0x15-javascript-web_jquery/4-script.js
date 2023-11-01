// Use jQuery to select the div with id toggle_header and add a click event handler
$('DIV#toggle_header').click(function() {
    // Within the click event handler, select the header element
    const header = $('header');

    // Toggle the classes red and green
    if (header.hasClass('red')) {
        header.removeClass('red');
        header.addClass('green');
    } else if (header.hasClass('green')) {
        header.removeClass('green');
        header.addClass('red');
    } else {
        // If the element has neither class, default to adding the red class
        header.addClass('red');
    }
});
