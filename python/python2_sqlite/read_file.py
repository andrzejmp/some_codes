#read_file.py
#go through data
f = open('data.csv')
#readlines returns a list
#of all lines of the file
lines = f.readlines()
result=[] #result - a list of lists
for line in lines:
    result.append(line.split(","))
#display 3 fields
for row in result:
    print row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]