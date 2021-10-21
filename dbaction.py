import sqlite3

def connect_db():
    connection_db = sqlite3.connect("results2.db")
    return connection_db

def add_db(a):
    cdb = connect_db()
    cursor_db = cdb.cursor()
    data = tuple(a)
    sentence_sql = "INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?)"
    cursor_db.execute(sentence_sql,(data))
    cdb.commit()
    cdb.close()


def delete_db(a):
    cdb = connect_db()
    cursor_db = cdb.cursor()

    if a == "N":
        sentence_sql = "DELETE FROM games WHERE idtype = 1"
    elif a == "L":
        sentence_sql = "DELETE FROM games WHERE idtype = 2"
    else:
        sentence_sql = "DELETE FROM games"

    cursor_db.execute(sentence_sql)
    cdb.commit()
    cdb.close()
