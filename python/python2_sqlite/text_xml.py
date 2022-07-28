#text_xml

import functions as func

f = open('data.csv')
output = func.get_countries(f)

w = open('data.xml','w')

s = '<?xml version="1.0" encoding="UTF-8"?>'
s += '<countries>'+'\n'

for row in output:
    country = row[0]
    continent = row[1]
    population = row[2]
    area = row[3]
    gdp1990 = row[4]
    gdp2000 = row[5]
    gdp2010 = row[6]
    fert_rate = row[7]
    expt_life = row[8]

    
    s += '<country>'+'\n' 
    
    s +=  '<name>'+country+'</name>'+'\n' 
    s +=  '<continent>'+continent+'</continent>'+'\n' 
    s +=  '<population>'+population+'</population>'+'\n' 
    s +=  '<area>'+area+'</area>'+'\n' 
    s +=  '<gdp1990>'+gdp1990+'</gdp1990>'+'\n' 
    s +=  '<gdp2000>'+gdp2000+'</gdp2000>'+'\n' 
    s +=  '<gdp2010>'+gdp2010+'</gdp2010>'+'\n' 
    s +=  '<fert_rate>'+fert_rate+'</fert_rate>'+'\n' 
    s +=  '<expt_life>'+expt_life+'</expt_life>'+'\n' 
    
    s += '</country>'+'\n' 



s += '</countries>'

w.write(s)
w.close()
    


