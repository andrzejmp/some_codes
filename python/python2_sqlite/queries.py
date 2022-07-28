#queries.py
#queries.py
sql1 = "DROP TABLE IF EXISTS continents;"
sql2 = '''    
       CREATE TABLE continents(
       continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
       continent_name TEXT NOT NULL
       );
       '''
sql3 = "DROP TABLE IF EXISTS countries;"
sql4 = '''
       CREATE TABLE countries(
        country_id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name TEXT NOT NULL,     
        population INT,
        area INT,   
        gdp_1990 INT,   
        gdp_2000 INT,   
        gdp_2010 INT,   
        fertility DOUBLE,
        life_exp DOUBLE,
        continent_id INTEGER NOT NULL REFERENCES continents(continent_id)
        );
        '''
