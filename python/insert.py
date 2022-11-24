from maria_baza import *

#insert_student(0,'s200', 'xxx', 'ko', "2022-03-05")

f = open('dane_a_p.csv')
lines=f.readlines()
for line in lines:
    line = line.strip()
    row = line.split(',')
    print(row)
    insert_student(0, 's'+row[0], row[1], row[2],  convert_date(row[3]))


