import psycopg2

from util.queries import get_l1_query, get_ln_query, get_rows_in_ln_query
from util.config import get_connection_config


def create_l1_table():
    query = get_l1_query()
    __exec_sql_command__(query)


def create_ln_table(n):
    query = get_ln_query(n)
    __exec_sql_command__(query)


def get_ln_row_count(n):
    query = get_rows_in_ln_query(n)
    conn = __get_pg_connection__()
    cur = conn.cursor()
    try:
        cur.execute(query)
        x = cur.fetchone()
        return x[0]
    except (Exception, psycopg2.DatabaseError) as e:
        print('Failed to execute query.')
        print(e)
    finally:
        cur.close()
        conn.close()


def __get_pg_connection__():
    params = get_connection_config()
    pg_connection = psycopg2.connect(**params)
    if pg_connection is not None:
        print("Established connection to PG")
    return pg_connection


def __exec_sql_command__(sql_query):
    conn = __get_pg_connection__()
    cur = conn.cursor()
    try:
        print(f'Executing query:\n {sql_query}\n...')
        cur.execute(sql_query)
        print('Query executed successfully!')
        conn.commit()
        print('TXN COMMITTED!')
    except (Exception, psycopg2.DatabaseError) as e:
        print('Failed to execute query.')
        print(e)
        conn.rollback()
        print('TXN ROLLED BACK!')
    finally:
        cur.close()
        conn.close()
