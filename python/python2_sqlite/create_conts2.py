#create the table ontinents
#create_conts2.py
 
import sqlite3 as lite
#polaczenie z baza danych
conn = lite.connect('world.db')
#stworzenie obiektu kursora
cur = conn.cursor()
 
sql1 = "DROP TABLE IF EXISTS continents;"
 
sql2 = '''    
       CREATE TABLE continents(
       continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
       continent_name TEXT NOT NULL
       );
       '''
with conn:
    cur.execute(sql1)
    cur.execute(sql2)
    print 'The table continents was created'