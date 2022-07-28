#test of module functions
#read_file3.py
import sys
import functions as func
f = open('data.csv')
output = func.get_countries(f)
get_continent = sys.argv[1]
min_density = float(sys.argv[2])

for row in output:
    country = row[0]
    continent = row[1]
    population = row[2]
    area = row[3]
    density = round(float(population) / float(area), 1)
    if continent == get_continent and density >= min_density:
        print '%-30s %10s %10s %10s' %(country, population, area, density)
  