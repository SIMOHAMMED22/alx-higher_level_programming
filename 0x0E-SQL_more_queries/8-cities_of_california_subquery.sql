-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- Select all cities of California without using JOIN
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
