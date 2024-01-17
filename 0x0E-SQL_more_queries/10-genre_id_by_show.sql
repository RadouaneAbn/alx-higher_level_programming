-- This script lists all shows contained in hbtn_0d_tvshows
-- That have at least one genre linked

SELECT ts.title, tsg.genre_id
	FROM tv_shows ts, tv_show_genres tsg
	WHERE tsg.show_id = ts.id
	ORDER BY ts.title ASC, tsg.genre_id ASC;
