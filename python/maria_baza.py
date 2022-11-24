import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='ap',
                                       user='MMMM',
                                       password='XXXX')
        if conn.is_connected():            
            #print('Connected to MySQL database')
            return conn

    except Error as e:
        print(e)

    

def insert_student(id, indeks, imie, nazwisko, data_skr):
    query = "INSERT INTO students(id, indeks, imie, nazwisko, data_dyp_skr) " \
            "VALUES(%s, %s,%s,%s,%s)"
    args = (id, indeks, imie, nazwisko, data_skr)

    try:
        #db_config = read_db_config()
        #conn = MySQLConnection(**db_config)
        conn = connect()

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

#---------------------------------------------------------------------------
def insert_nowe(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod):
    query = "INSERT INTO nowe1(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod) " \
            "VALUES(%s, %s,%s,%s,%s,%s,%s)"
    args = (id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod)

    try:        
        conn = connect()

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def insert_nowe2(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod):
    query = "INSERT INTO nowe2(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod) " \
            "VALUES(%s, %s,%s,%s,%s,%s,%s)"
    args = (id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod)

    try:        
        conn = connect()

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_nowe3(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod):
    query = "INSERT INTO nowe3(id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod) " \
            "VALUES(%s, %s,%s,%s,%s,%s,%s)"
    args = (id, nazwisko, imie, prywatny, sluzbowy, indeks, prg_kod)

    try:        
        conn = connect()

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()





#-----------------------------------------------------

def convert_date(str_date):
    converted_date = str_date[6:]+'.'+str_date[3:5]+'.'+str_date[0:2]
    return converted_date




