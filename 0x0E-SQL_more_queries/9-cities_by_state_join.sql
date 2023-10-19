-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- Select all cities with their corresponding state names
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
