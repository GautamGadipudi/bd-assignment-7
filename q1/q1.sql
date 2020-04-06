DROP TABLE IF EXISTS popular_movie_actors;

CREATE TABLE IF NOT EXISTS popular_movie_actors(
	movie INTEGER NOT NULL,
	actor INTEGER NOT NULL,
	PRIMARY KEY(movie, actor),
	FOREIGN KEY(movie) REFERENCES movie(id),
	FOREIGN KEY(actor) REFERENCES member(id)
);

INSERT INTO popular_movie_actors(movie, actor)
SELECT 
movie, actor
FROM Movie_Actor ma
INNER JOIN (
			SELECT id,
			avgRating
			FROM 
			Movie
		   	WHERE type = 'movie'
		   		AND avgRating > 5
		   ) AS m
		ON m.id = ma.movie;