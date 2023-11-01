// Use jQuery to select the div with id add_item and add a click event handler
$('DIV#add_item').click(function() {
    // Within the click event handler, select the ul element with the class my_list and append a new li element
    $('ul.my_list').append('<li>Item</li>');
});
