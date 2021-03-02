-- lists all genres of the show Dexter
-- displays tv_genres.name
SELECT tv_genres.name FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_shows.title = 'Dexter' AND tv_shows.id = tv_show_genres.show_id
AND tv_genres.id = tv_show_genres.genre_id;