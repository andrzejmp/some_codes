#functions.py

def get_countries(fin):
    '''
    Reads a text file with fields separeted
    by comma and returns a list of rows.
    Each row a is a list and represents
    one line from a text file.
    '''
    result = []
    lines = fin.readlines()
    for line in lines:
        row = []
        row = line.split(",")
        result.append(row)
    return result[1:]

def text_to_list(fin):  
    '''
    Reads a text file with fields separeted 
    by semicolon and returns a list of rows.
    Each row a is a list and represents 
    one line from a text file.  
    '''
    result = [] 
    lines = fin.readlines()
    for line in lines:      
        row = []
        row = line.split(";")
        result.append(row)
    return result
	
def connect_to_sqlite(dbname):
    import sqlite3 as lite
    #create the connection to the database
    conn = lite.connect(dbname)
    return conn

def insert_to_countries1(nam, pop, are, p_90, p_00, p_10, fert, life, cont_id):
    s = '''INSERT INTO  countries (country_name, population, area, gdp_1990, gdp_2000, 
           gdp_2010, fertility, life_exp, continent_id) 
           VALUES ('%s',%s, %s, %s, %s, %s, %s, %s, %s);
        '''  % (nam, pop, are, p_90, p_00, p_10, fert, life, cont_id)
    return s

s = '''INSERT INTO  countries (country_name, population, area, gdp_1990, gdp_2000, gdp_2010, fertility, life_exp, continent_id) 
       VALUES (:nam, :pop, :are, :p_90, :p_00, :p_10, :fert, :life, :cont_id);
    ''' 