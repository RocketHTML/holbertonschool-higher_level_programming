-- list all genres not of the show Dexter
SELECT name from tv_genres
WHERE name NOT IN
(SELECT name FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter')
ORDER BY name ASC;
