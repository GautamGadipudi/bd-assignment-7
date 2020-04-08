from q5.util.constants import L1_TABLE_NAME, DEFAULT_MINIMUM_SUPPORT


def get_l1_query(table_name=L1_TABLE_NAME, min_support=DEFAULT_MINIMUM_SUPPORT):
    query = f'''DROP TABLE IF EXISTS {table_name};

                CREATE TABLE IF NOT EXISTS {table_name}(
                    actor INTEGER NOT NULL,
                    count INTEGER NOT NULL,
                    PRIMARY KEY(actor),
                    FOREIGN KEY(actor) REFERENCES member(id)
                );
                
                WITH ROWS as (
                INSERT INTO {table_name}
                SELECT 
                actor,
                COUNT(movie)
                FROM popular_movie_actors
                GROUP BY actor
                HAVING COUNT(movie) >= {str(min_support)}
                RETURNING 1)
                SELECT COUNT(*) FROM ROWS'''

    return query
