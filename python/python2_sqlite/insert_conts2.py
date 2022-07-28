#populating of the table continents
#insert_conts2.py
 
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
 
sql = "INSERT INTO  continents (continent_name) VALUES (:cont)"
     
#execute the SQL queries or statements
with conn:
    for c in conts:
        cur.execute(sql, {'cont':c})
        print c + ' inserted.'