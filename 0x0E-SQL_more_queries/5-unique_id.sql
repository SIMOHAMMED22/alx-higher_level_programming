-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- Create or update the 'id_not_null' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Note: Make sure to replace 'your_admin_username' and 'your_database_name' with the actual MySQL administrative username and the desired database name.
