-- This script creates a user 'holberton_user' with the password 'projectcorrection280hbtn'
-- It grants the 'REPLICATION CLIENT' privilege to the user on all databases
-- Finally, it flushes the privileges to ensure the changes take effect

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
