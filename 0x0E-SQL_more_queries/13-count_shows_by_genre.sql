-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each
SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
