/*
    Author: Gautam Gadipudi
    RIT Id: gg7148@rit.edu
*/

DROP TABLE IF EXISTS L2;

CREATE TABLE IF NOT EXISTS L2(
	actor1 INTEGER NOT NULL,
	actor2 INTEGER NOT NULL,
	count INTEGER NOT NULL,
	PRIMARY KEY(actor1, actor2),
	FOREIGN KEY(actor1) REFERENCES member(id),
	FOREIGN KEY(actor2) REFERENCES member(id)
);

INSERT INTO L2
SELECT 
pma.actor AS actor1,
pma2.actor AS actor2,
COUNT(pma.movie)
FROM popular_movie_actors AS pma
INNER JOIN L1
	ON L1.actor = pma.actor
INNER JOIN popular_movie_actors AS pma2
	ON pma2.movie = pma.movie
	AND pma2.actor > pma.actor
GROUP BY actor1, actor2
HAVING COUNT(pma.movie) >= 5