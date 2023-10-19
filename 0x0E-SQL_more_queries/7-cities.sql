-- Connect to the MySQL server
-- You can use the following command to connect to the MySQL server:
-- mysql -u your_admin_username -p

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'cities' table if it doesn't already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Note: Make sure to replace 'your_admin_username' with the actual MySQL administrative username.
