-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
