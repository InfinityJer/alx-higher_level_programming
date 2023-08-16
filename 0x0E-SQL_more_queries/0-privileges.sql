-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Create user user_0d_1 if it doesn't exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
