from multiprocessing import connection
from socket import create_connection
import sqlite3
from sqlite3 import Error
from venv import create

def create_connection(db):
    conn=None
    try:
        conn=sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn,table):
    try:
        c=conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)

def support():
    database= r"C:\sqlite\db\vnewdb.db"
    sql_table_Movies="""create table if not exists Movies(
                            mNo integer primary key,
                            name text NOT NULL,
                            actor tex,
                            actress text,
                            director text NOT NULL,
                            year_of_release text
                    );"""
    conn=create_connection(database)
    if conn is not None:
        create_table(conn,sql_table_Movies)
    else:
        print("Connetion cannot be made")

if __name__ == "__main__":
    support()