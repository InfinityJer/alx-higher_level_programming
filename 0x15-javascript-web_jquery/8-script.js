// Use jQuery to fetch data from the specified URL using the get method
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Within the callback function, iterate through the results and append each movie title to the list
    data.results.forEach(function(movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
});
