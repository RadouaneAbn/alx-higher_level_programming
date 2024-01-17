-- This script the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT exists hbtn_0d_usa;

CREATE TABLE IF NOT exists hbtn_0d_usa.cities (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL);
