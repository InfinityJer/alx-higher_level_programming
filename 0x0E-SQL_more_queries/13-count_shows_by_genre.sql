-- Count the number of shows per genre in hbtn_0d_tvshows
SELECT g.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS tsg ON g.id = tsg.genre_id
GROUP BY g.id, g.name
ORDER BY g.name;
