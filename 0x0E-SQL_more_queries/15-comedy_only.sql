-- lists all Comedy shows in the database hbtn_0d_tvshows
-- displays tv_shows.title
SELECT tv_shows.title FROM tv_genres, tv_shows, tv_show_genres
WHERE tv_genres.name = 'Comedy' AND tv_shows.id = tv_show_genres.show_id
AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
