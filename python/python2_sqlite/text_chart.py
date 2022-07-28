#save data in Excel file
#text_excel.py

import sys

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


import functions as func

f = open('data.csv')
output = func.get_countries(f)

get_continent = sys.argv[1]
min_density = float(sys.argv[2])

countries = []
list_density = []
for row in output:
    country = row[0]
    continent = row[1]
    population = row[2]
    area = row[3]
    density = round(float(population) / float(area), 1)
    if continent == get_continent and density >= min_density:
        print '%-30s %10s %10s %10s' %(country, population, area, density)
        countries.append(country)
        list_density.append(density)

countries = tuple(countries)

plt.rcdefaults()
fig, ax = plt.subplots()

number = len(countries)
y_pos = np.arange(number)
#error = np.random.rand(len(countries))

ax.barh(y_pos, list_density, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(countries)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('people per square km')
ax.set_title( str(number) + ' most densely populated countries in ' + get_continent)

plt.show()