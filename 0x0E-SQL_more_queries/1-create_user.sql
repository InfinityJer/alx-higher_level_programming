-- Create the MySQL server user user_0d_1 if it doesn't exist
-- Grant all privileges to user_0d_1 on the entire MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
