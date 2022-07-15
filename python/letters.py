#letters.py
# -*- coding: utf-8 -*-

s = '''
To Sherlock Holmes she is always the woman. I have seldom heard him mention her under
any other name. In his eyes she eclipses and predominates the whole of her sex.
It was not that he felt any emotion akin to love for Irene Adler. All emotions,
and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen,
but as a lover he would have placed himself in a false position.
From Adventures of Sherlock Holmes by Arthur Conan Doyle'''

chars = []
for i in range(255):
    chars.append(0)

for letter in s:
    indeks=ord(letter)-1
    chars[indeks]+=1

d = len(chars)
X = []
Y = []

for i in range(d):
    if chars[i]>0 and (i+1)>=97 and (i+1)<=122:
        X.append(chr(i+1))
        Y.append(chars[i])

#print (Y)
sum_y = sum(Y)
print ('All small letters in the text: ', sum_y)
print ('\nThe frequency of letters in %:\n ')

for i in range(len(X)):
    Y[i] = round(100.0*Y[i]/sum_y,1)
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

