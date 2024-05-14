-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Use the tyrell_corp database
USE tyrell_corp;

-- Create the nexus6 table with an auto-incrementing id and a name column
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert a row into the nexus6 table with the name 'Leon'
INSERT INTO nexus6 (name) VALUES ('Leon');

-- Grant SELECT permission on the nexus6 table to the 'holberton_user'@'localhost' user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
