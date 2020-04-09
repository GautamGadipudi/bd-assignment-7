/*
    Author: Gautam Gadipudi
    RIT Id: gg7148@rit.edu
*/

DROP TABLE IF EXISTS L1;

CREATE TABLE IF NOT EXISTS L1(
	actor INTEGER NOT NULL,
	count INTEGER NOT NULL,
	PRIMARY KEY(actor),
	FOREIGN KEY(actor) REFERENCES member(id)
);

INSERT INTO L1
SELECT 
actor,
COUNT(movie)
FROM popular_movie_actors
GROUP BY actor
HAVING COUNT(movie) >= 5