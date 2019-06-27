import sqlite3 as sql

def insertcontactcs(contact_id, fullname, phone, email):
    con = sql.connect("DB/baseFlask.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO contacts VALUES(?, ?, ?, ?)", (contact_id, fullname, phone, email))
    con.commit()
    con.close()

def consulta():
    con = sql.connect("DB/baseFlask.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM contacts")
    datos = cursor.fetchall()
    print(datos)
    con.commit()
    con.close()
    return datos
