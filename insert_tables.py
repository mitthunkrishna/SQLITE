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

def create_Movie(conn,task):
    sql='''insert into Movies(
        mNo,name,actor,actress,director,year_of_release) values(?,?,?,?,?,?)'''
    cur=conn.cursor()

    cur.execute(sql,task)
    conn.commit()
    return cur.lastrowid


def support():
    database= r"C:\sqlite\db\vnewdb.db"
    
    conn=create_connection(database)
    with conn:
        task_1=('1','Darbar','Rajinikanth','Nayanthara','AR Muragadoss','2020')
        task_2=('2','Petta','Rajinikanth','Simran','Karthick Subraj','2019')
        task_3=('3','Theri','Vijay','Samantha','Atlee','2016')
        create_Movie(conn,task_1)
        create_Movie(conn,task_2)
        create_Movie(conn,task_3)
if __name__ == "__main__":
    support()