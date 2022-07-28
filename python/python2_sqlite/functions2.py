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