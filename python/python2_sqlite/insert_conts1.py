#populating of the table continents
#insert_conts1.py
 
import functions as func
 
f = open('data.txt')
output = func.text_to_list(f)
conts=[]
for row in output:
    conts.append(row[1])
#set removes duplicates
conts = sorted(list(set(conts)))
 
#connection to the database
conn = func.connect_to_sqlite('world.db')
cur = conn.cursor()
 
sql = "INSERT INTO  continents (continent_name) VALUES (?)"
     
#execute the SQL queries or statements
with conn:
    for c in conts:
        cur.execute(sql, (c,))
        print c + ' inserted.'