-- This script lists all genres from hbtn_0d_tvshows

SELECT tg.name AS genre, count(tsg.genre_id) AS number_of_shows
	FROM tv_genres tg
	RIGHT JOIN tv_show_genres tsg
	ON tg.id = tsg.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
