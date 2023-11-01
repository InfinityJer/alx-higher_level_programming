// Use jQuery to fetch data from the specified URL using the get method
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Within the callback function, select the div with id character and set its text to the character's name
    $('DIV#character').text(data.name);
});
