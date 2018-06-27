-- Counts the number of TV shows in each genre
SELECT name AS genre, COUNT(*) AS number_shows
FROM tv_genres
LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING number_shows >= 1
ORDER BY number_shows DESC;
