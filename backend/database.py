import psycopg
from psycopg import sql
import os
import sys


def get_login(conn, email):
    try:
        with conn.cursor() as cur:
            
            query = sql.SQL("SELECT {fields} FROM {table} WHERE {key} = {email}").format(fields=sql.SQL(',').join([sql.Identifier('email'), 
                                                          sql.Identifier('password')]), table=sql.Identifier('users'), key=sql.Identifier('email'), email=email).as_string(conn)
            print(query)
            cur.execute(query)
            
            return cur.fetchone()
    except psycopg.Error as e:
        raise e
    
    
    


if __name__ == "__main__":
    conn = psycopg.connect(host="localhost", port=5432, dbname="Threadnotes",connect_timeout=10)
    test_email = "test1@gmail.com"
    test_password = "xa3f59u0"
    
    if sys.argv[1] == 'get_login':
        print(get_login(conn, test_email))