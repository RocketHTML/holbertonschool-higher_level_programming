-- We only want comedy shows
SELECT title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = show_id
INNER JOIN tv_genres ON genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY title ASC;
