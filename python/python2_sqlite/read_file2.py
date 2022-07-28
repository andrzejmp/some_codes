#test of module functions
#read_file2.py
import functions as func
f = open('data.csv')
output = func.get_countries(f)

for row in output:
    print '%-30s %10s %10s %10s' %(row[0], row[2], row[3],  round(float(row[2]) / float(row[3]) ,1))
    