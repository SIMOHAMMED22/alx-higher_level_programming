-- Connect to the MySQL server
-- You can use the following command to connect to the MySQL server:
-- mysql -u your_admin_username -p

-- Create or update user user_0d_1 with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
