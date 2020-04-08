from q5.util.constants import L1_TABLE_NAME, MINIMUM_SUPPORT


def get_l1_query(tablename=L1_TABLE_NAME, min_support=MINIMUM_SUPPORT):
    query = f'''DROP TABLE IF EXISTS {tablename};

                CREATE TABLE IF NOT EXISTS {tablename}(
                    actor INTEGER NOT NULL,
                    count INTEGER NOT NULL,
                    PRIMARY KEY(actor),
                    FOREIGN KEY(actor) REFERENCES member(id)
                );
                
                INSERT INTO {tablename}
                SELECT 
                actor,
                COUNT(movie)
                FROM popular_movie_actors
                GROUP BY actor
                HAVING COUNT(movie) >= {str(min_support)}'''

    return query
