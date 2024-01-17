-- This script lists all cities contained in the database hbtn_0d_usa

SELECT c.id, c.name, s.name
	FROM states s, cities c
	WHERE c.state_id = s.id
	ORDER BY c.id ASC;
