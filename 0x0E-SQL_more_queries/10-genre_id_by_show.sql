-- lists all shows contained in database that have at least one genre linked
SELECT DISTINCT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
