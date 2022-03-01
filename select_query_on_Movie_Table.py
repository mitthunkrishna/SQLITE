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

def select_with_actor(conn,actor):
    cur=conn.cursor()
    cur.execute("SELECT * FROM Movies WHERE actor=?",(actor,))
    rows=cur.fetchall()
    for row in rows:
        print(row)

def select_all(conn):
    cur=conn.cursor()
    cur.execute("SELECT * FROM Movies")
    rows=cur.fetchall()

    for row in rows:
        print(row)

def support():
    database= r"C:\sqlite\db\vnewdb.db"
    conn=create_connection(database)
    with conn:
        print("Select all:")
        select_all(conn)

        print("Select all movies which are acted by rajinikanth:")
        select_with_actor(conn,"Rajinikanth")

if __name__ == "__main__":
    support()