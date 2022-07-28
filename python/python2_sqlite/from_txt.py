#! /usr/bin/python
#from_txt.py
import functions as func

#creating the list of continents
f = open('data.txt')
output = func.text_to_list(f)
conts=[]
for row in output:
    conts.append(row[1])
conts = sorted(list(set(conts)))

conn = func.connect_to_sqlite('world.db')
cur = conn.cursor()

#execute the SQL statement
s = '''INSERT INTO  countries (country_name, population, area, gdp_1990, gdp_2000, gdp_2010, fertility, life_exp, continent_id) 
        VALUES (:nam, :pop, :are, :p_90, :p_00, :p_10, :fert, :life, :cont_id);
    '''   		 	


with conn:
    for row in output:				
        par = {'nam':row[0], 'pop':row[2], 'are':row[3], 'p_90':row[4], 'p_00':row[5], 'p_10':row[6], 'fert':row[7], 'life':row[8], 'cont_id':(conts.index(row[1])+1)}			
        cur.execute(s, par)
		
	cur.execute("update countries set gdp_1990 = NULL where length(gdp_1990) = 0")
	cur.execute("update countries set gdp_2000 = NULL where length(gdp_2000) = 0")
	cur.execute("update countries set gdp_2010 = NULL where length(gdp_2010) = 0")

		
print 'done!'




















	

