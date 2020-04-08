import pandas as pd
import psycopg2

from q5.config.pg import get_connection_config

def __get_pg_connection__():
    params = get_connection_config()
    pg_connection = psycopg2.connect(**params)
    if pg_connection is not None:
        print("Established connection to PG")
    return pg_connection

def get_pandas_table(sql_query):
    conn = __get_pg_connection__()
    try:
        table = pd.read_sql_query(sql_query, conn)
        return table
    except Exception as e:
        print(e)
    finally:
        conn.close()


def create_l1_table(tablename='level_1'):




def exec_SQL_command(sql_query):
    conn = __get_pg_connection__()
    cur = conn.cursor()
    try:
        print(f'Executing query {sql_query}\n...')
        cur.execute(sql_query)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
