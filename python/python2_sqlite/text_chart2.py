#text_chart2
#pie chart

import matplotlib.pyplot as plt
import functions as func

f = open('data.csv')
output = func.get_countries(f)

conts=[]
for row in output:
    conts.append(row[1])

conts = list(set(conts))

cont_pop = {}
for c in conts:
    cont_pop[c] = 0

for row in output:
    continent = row[1]
    population = int(row[2])
    cont_pop[continent] += population

for k in cont_pop:
    print k, cont_pop[k]

conts = cont_pop.keys()
slices = cont_pop.values()

cols = ['g','m','r','y','b','c']

plt.pie(slices,
        labels=conts,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0,0,0),
        autopct='%1.1f%%')
        
plt.title('Population of continents [in %]\n2015 year')
plt.show()






