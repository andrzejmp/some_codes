#create the table ontinents
#create_conts1.py
 
import sqlite3 as lite
#polaczenie z baza danych
conn = lite.connect('world.db')
#stworzenie obiektu kursora
cur = conn.cursor()
 
sql = '''
      CREATE TABLE continents(
      continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
      continent_name TEXT NOT NULL
      );
      '''
with conn:
    cur.execute(sql)
    print 'The table continents was created'