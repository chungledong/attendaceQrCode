import sqlite3
from sqlite3 import Error


def sql_connection(database):
    conn = None
    try:
        con = sqlite3.connect(database)
        return con
    except Error as e:
        print(e)

def sql_insert(database, sql, entities):
    try:
        con = sqlite3.connect(database)
        cursorObje = con.cursor()
        cursorObje.execute(sql, entities)
        con.commit()
    except Error as e:
        print(e)

def sql_update(con, sql, entities):
    try:
        cursorObje = con.cursor()
        cursorObje.execute(sql, entities)
        con.commit()
    except Error as e:
        print(e)

def sql_fetch(con, sql):
    try:
        cursorObje = con.cursor()
        cursorObje.execute(sql)
        rows = cursorObje.fetchall()

        return rows
    except Error as e:
        print(e)

#if __name__ == '__main__':
    #db = 'Attendance.db'
    #con = sqlite3.connect(db)
    #cursorObj = con.cursor()

    #cursorObj.execute('SELECT * FROM tblEmployees')
    #rows = cursorObj.fetchall()
    #con = sql_connection(db)
    #rows = sql_fetch(con, 'SELECT * FROM tblEmployees')
    #for row in rows:
        #print(row)
        #print(row[0])
