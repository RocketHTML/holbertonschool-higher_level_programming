-- lists all tv shows and genre id's in database, displays NULL for shows with no genre_id
SELECT title, genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id; 
