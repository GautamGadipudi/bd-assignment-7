import pandas as pd
import psycopg2
from configparser import ConfigParser

from q5.util.constants import PG_CONNECTION_CONFIG_FILE_PATH, PG_CONNECTION_CONFIG_SECTION
from q5.util.queries import get_l1_query


def get_connection_config(filename=PG_CONNECTION_CONFIG_FILE_PATH, section=PG_CONNECTION_CONFIG_SECTION):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the file {filename}')
    return db


def get_pandas_table(sql_query):
    conn = __get_pg_connection__()
    try:
        table = pd.read_sql_query(sql_query, conn)
        return table
    except Exception as e:
        print(e)
    finally:
        conn.close()


def create_l1_table():
    query = get_l1_query()
    __exec_sql_command__(query)


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
        x = ()
        if cur.rowcount > 0:
            x = cur.fetchall()
        conn.commit()
        print(str(x[0][0]) + ' rows affected.')
        print('Query executed successfully!')
    except (Exception, psycopg2.DatabaseError) as e:
        print('Failed to execute query.')
        print(e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
