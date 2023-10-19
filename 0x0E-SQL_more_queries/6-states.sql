-- Connect to the MySQL server and specify the database
-- You can use the following command to connect to the MySQL server with the specified database:
-- mysql -u your_admin_username -p your_database_name

-- Create or update the 'unique_id' table if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, name VARCHAR(256) NOT NULL);

-- Note: Make sure to replace 'your_admin_username' and 'your_database_name' with the actual MySQL administrative username and the desired database name.
