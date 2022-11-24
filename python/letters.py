#letters.py
# -*- coding: utf-8 -*-

s = '''
Ukraiński portal opisał niecodzienną sytuację spod Lwowa. Lokalny kierowca realizował codzienny kurs, gdy jedna z pasażerek zaczęła wykrzykiwać prorosyjskie hasła. Początkowo nic nie robił sobie ze słów kobiety, tylko prosił, żeby nie przeszkadzała innym. Jednak zachowanie kobiety było coraz bardziej agresywne, nie chciała się uspokoić, zaczęła krzyczeć. 
'''

chars = []
for i in range(455):
    chars.append(0)

for letter in s:
    indeks=ord(letter)-1
    chars[indeks]+=1

d = len(chars)
X = []
Y = []

for i in range(d):
    #if chars[i]>0 and (i+1)>=97 and (i+1)<=122:
    #    X.append(chr(i+1))
    #    Y.append(chars[i])
    if chars[i]>0 and (i+1)>=64:
        X.append(chr(i+1))
        Y.append(chars[i])

#print (Y)
sum_y = sum(Y)
print ('All small letters in the text: ', sum_y)
print ('\nThe frequency of letters in %:\n ')

for i in range(len(X)):
    Y[i] = round(100.0*Y[i]/sum_y,1)
    if Y[i] > 0:
        print ('%5s %10.1f' %(X[i], Y[i]))

from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("letters_freq.html")
p = figure(x_range=X, height=250, title="Letters Frequences in English Text",
           toolbar_location=None, tools="")

p.vbar(x=X, top=Y, width=0.4)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)

#https://pynative.com/python-mysql-select-query-to-fetch-data/#h-steps-to-fetch-rows-from-a-mysql-database-table