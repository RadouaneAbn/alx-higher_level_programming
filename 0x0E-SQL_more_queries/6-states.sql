-- This script creates the database hbtn_0d_usa and the table states

CREATE DATABASE IF NOT exists hbtn_0d_usa;

CREATE TABLE IF NOT exists hbtn_0d_usa.states (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL);
