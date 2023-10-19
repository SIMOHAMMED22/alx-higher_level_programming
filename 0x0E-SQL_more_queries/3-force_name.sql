-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- Create or update the 'force_name' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Note: Make sure to replace 'your_admin_username' and 'your_database_name' with the actual MySQL administrative username and the desired database name.
