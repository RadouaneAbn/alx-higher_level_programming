-- This script lists all the cities of California
-- that can be found in the database hbtn_0d_usa

SELECT c.id, c.name
	FROM states s, cities c
	WHERE c.state_id = s.id
	AND s.name = "California";
