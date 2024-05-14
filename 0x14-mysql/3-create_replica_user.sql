-- Create replica user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user';

-- Grant replication slave privileges to replica user
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant select privileges on mysql.user table to holberton_user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
