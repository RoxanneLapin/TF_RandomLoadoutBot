import sqlite3



def get_data_class(database : str):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM player_class")
    res =  cur.fetchall()
    cur.close()


    return res

def get_data_for_class(database : str, table : str, player_class_name : str):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(f"SELECT t.* FROM {table} t JOIN player_class c ON t.player_class = c.id  WHERE LOWER(c.name)=LOWER('{player_class_name}')")
    res = cur.fetchall()
    cur.close()

    return res





