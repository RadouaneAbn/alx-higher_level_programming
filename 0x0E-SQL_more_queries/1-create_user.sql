-- This script creates a MySQL server user user_0d_1

CREATE USER IF NOT exists 'user_0d_1'@'localhost'
	IDENTIFIED WITH auth_socket
	BY "user_0d_1_pwd";

GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost';
