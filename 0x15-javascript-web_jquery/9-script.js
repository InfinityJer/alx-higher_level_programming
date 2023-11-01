// Use jQuery to fetch data from the specified URL with the lang parameter set to 'fr' using the get method
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Within the callback function, select the div with id hello and set its text to the fetched translation
    $('DIV#hello').text(data.hello);
});
