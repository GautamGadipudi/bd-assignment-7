'''
    Author: Gautam Gadipudi
    RIT Id: gg7148
'''

from util.constants import *


def get_l1_query(table_name=L1_TABLE_NAME, min_support=DEFAULT_MINIMUM_SUPPORT):
    query = f'''DROP TABLE IF EXISTS {table_name};

                CREATE TABLE IF NOT EXISTS {table_name}(
                    actor0 INTEGER NOT NULL,
                    count INTEGER NOT NULL,
                    PRIMARY KEY(actor0),
                    FOREIGN KEY(actor0) REFERENCES member(id)
                );
                
                WITH ROWS as (
                INSERT INTO {table_name}
                SELECT 
                actor AS actor0,
                COUNT(movie)
                FROM popular_movie_actors
                GROUP BY actor
                HAVING COUNT(movie) >= {str(min_support)}
                RETURNING 1)
                SELECT COUNT(*) FROM ROWS'''

    return query


def get_ln_query(n, min_support=DEFAULT_MINIMUM_SUPPORT):
    prev_level_table_name = f'level_{n - 1}'
    drop_statement = f'DROP TABLE IF EXISTS level_{n};\n'
    select_statement = f'SELECT '
    for i in range(n):
        select_statement += f'{MAIN_TABLE_ALIAS}{i}.{MAIN_TABLE_ACTOR_FIELD} AS {MAIN_TABLE_ACTOR_FIELD}{i},\n'
    select_statement += f'COUNT({MAIN_TABLE_ALIAS}0.{MAIN_TABLE_MOVIE_FIELD})\n'

    pma_union_list = []
    for i in range(n - 1):
        partial_query = f'''SELECT {MAIN_TABLE_ALIAS}.{MAIN_TABLE_ACTOR_FIELD}, 
                                    {MAIN_TABLE_MOVIE_FIELD}
                            FROM {MAIN_TABLE} AS {MAIN_TABLE_ALIAS}
                            INNER JOIN {prev_level_table_name}
                                ON {prev_level_table_name}.{MAIN_TABLE_ACTOR_FIELD}{i} = {MAIN_TABLE_ALIAS}.{MAIN_TABLE_ACTOR_FIELD}'''
        pma_union_list.append(partial_query)
    pma_union_statement = ' UNION '.join(pma_union_list)

    pma_join_list = []
    for i in range(n - 1):
        partial_query = f'''INNER JOIN {MAIN_TABLE} AS {MAIN_TABLE_ALIAS}{i + 1}
                                ON {MAIN_TABLE_ALIAS}{i + 1}.{MAIN_TABLE_MOVIE_FIELD} = {MAIN_TABLE_ALIAS}{i}.{MAIN_TABLE_MOVIE_FIELD} 
                                AND {MAIN_TABLE_ALIAS}{i + 1}.{MAIN_TABLE_ACTOR_FIELD} > {MAIN_TABLE_ALIAS}{i}.{MAIN_TABLE_ACTOR_FIELD}'''
        pma_join_list.append(partial_query)
    pma_join_statement = ' '.join(pma_join_list)

    group_by_list = []
    for i in range(n):
        partial_query = f'{MAIN_TABLE_ACTOR_FIELD}{i}'
        group_by_list.append(partial_query)
    group_by_statement = 'GROUP BY '
    group_by_statement += ', '.join(group_by_list)

    having_statement = f'HAVING COUNT({MAIN_TABLE_ALIAS}0.{MAIN_TABLE_MOVIE_FIELD}) >= {min_support}'

    result = f'''
        {drop_statement}
        {select_statement}
        INTO TABLE level_{n}
        FROM
        ({pma_union_statement}) AS {MAIN_TABLE_ALIAS}0
        {pma_join_statement}
        {group_by_statement}
        {having_statement}
    '''

    return result


def get_rows_in_ln_query(n):
    return f'SELECT COUNT(*) FROM level_{n};'


def get_final_query(n):
    table_name = f'level_{n}'
    new_table_name = 'final_level'
    drop_statement = f'DROP TABLE IF EXISTS {new_table_name};\n'
    select_statement = 'SELECT \n'
    for i in range(n):
        select_statement += f'm{i}.name AS actor{i},\n'
    select_statement += ' count'

    join_statement = ''
    for i in range(n):
        join_statement += f''' INNER JOIN member m{i} ON m{i}.id=actor{i} '''

    result = f'''
        {drop_statement}
        {select_statement}
        INTO TABLE {new_table_name}
        FROM
        {table_name}
        {join_statement}
    '''

    return result