-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- List genres and the number of linked shows for each genre
SELECT tv_show_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
