DROP TABLE IF EXISTS L3;

CREATE TABLE IF NOT EXISTS L3(
	actor1 INTEGER NOT NULL,
	actor2 INTEGER NOT NULL,
	actor3 INTEGER NOT NULL,
	count INTEGER NOT NULL,
	PRIMARY KEY(actor1, actor2, actor3),
	FOREIGN KEY(actor1) REFERENCES member(id),
	FOREIGN KEY(actor2) REFERENCES member(id),
	FOREIGN KEY(actor3) REFERENCES member(id)
);

INSERT INTO L3
SELECT 
	pma.actor AS actor1,
	pma2.actor AS actor2,
	pma3.actor AS actor3,
	COUNT(pma.movie)
FROM
(
	SELECT 
		pma1.actor, 
		movie
	FROM popular_movie_actors AS pma1
	INNER JOIN L2
		ON L2.actor1 = pma1.actor
	
	UNION
	
	SELECT
		pma2.actor, 
		movie
	FROM popular_movie_actors AS pma2
	INNER JOIN L2
		ON L2.actor2 = pma2.actor
) AS pma
INNER JOIN popular_movie_actors AS pma2
	ON pma2.movie = pma.movie
	AND pma2.actor > pma.actor
INNER JOIN popular_movie_actors AS pma3
	ON pma3.movie = pma.movie
	AND pma3.actor > pma2.actor
GROUP BY actor1, actor2, actor3
HAVING COUNT(pma.movie) >= 5