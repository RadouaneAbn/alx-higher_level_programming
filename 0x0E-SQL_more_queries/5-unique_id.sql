-- This script creates teh table unique_id

CREATE TABLE IF NOT exists unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
