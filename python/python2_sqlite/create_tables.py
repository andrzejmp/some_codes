#create the tables continents, countries
#create_tables.py
import functions as func
import queries as q
#polaczenie z baza danych
conn = func.connect_to_sqlite('world.db')
#stworzenie obiektu kursora
cur = conn.cursor()
 
#stworzenie tabel
with conn:
    cur.execute(q.sql1)
    cur.execute(q.sql2)
    cur.execute(q.sql3)
    cur.execute(q.sql4)
    print 'Tables continents and countries created'
