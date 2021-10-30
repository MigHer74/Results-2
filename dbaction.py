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


def change_db(selg):
    cdb = connect_db()
    cursor_db = cdb.cursor()

    if selg == "N":
        script_sql = open("script_s.sql")
    else:
        script_sql = open("script_l.sql")
    
    script_var = script_sql.read()
    cursor_db.executescript(script_var)
    cdb.commit()
    cdb.close()


def view_db(vsel):
    cdb = connect_db()
    cursor_db = cdb.cursor()

    if vsel == "N":
        sentence_sql = "SELECT * FROM games WHERE idtype = 'A' ORDER BY idtype, gameweek, gametype"
    elif vsel == "L":
        sentence_sql = "SELECT * FROM games WHERE idtype = 'B' ORDER BY idtype, gameweek, gametype"
    else:
        sentence_sql = "SELECT * FROM games ORDER BY idtype, gameweek, gametype"
    
    cursor_db.execute(sentence_sql)
    
    data = cursor_db.fetchall()
    
    cdb.close()

    return data


def delete_db(a):
    cdb = connect_db()
    cursor_db = cdb.cursor()

    if a == "S":
        cursor_db.execute("DELETE FROM games WHERE idtype = 'A'")
        ok_mess = "DATA DELETED SUCCESSFULLY"
    elif a == "L":
        cursor_db.execute("DELETE FROM games WHERE idtype = 'B'")
        ok_mess = "DATA DELETED SUCCESSFULLY"
    elif a == "A":
        cursor_db.execute("DELETE FROM games")
        ok_mess = "DATA DELETED SUCCESSFULLY"
    else:
        ok_mess = "OPERATION CANCELLED"

    input(f"\n{ok_mess}\nPress any key to continue...")

    cdb.commit()
    cdb.close()
