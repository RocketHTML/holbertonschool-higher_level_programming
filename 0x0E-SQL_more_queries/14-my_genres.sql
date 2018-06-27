-- list all genres of the show Dexter
SELECT tv_genres.name as name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = show_id
INNER JOIN tv_genres ON genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
