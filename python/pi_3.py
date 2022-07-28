# -*- coding: utf-8 -*-
"""
Created on Mon May 08 20:15:30 2017
@author: Andrzej
"""
#obliczanie liczby pi

def pi1(n):
    Y=[]
    X=[]
    Z=[]
    s = 0
    for i in range(1,n+1):
        s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
        X.append(i)
        Y.append(round(s,2))
        Z.append(3.14)
    return X, Y, Z        

#50 iteracji            
X, Y, Z = pi1(50)

from bokeh.plotting import figure, output_file, show

output_file("liczba_pi1.html")

p = figure(title="Wyznaczanie liczby Pi", x_axis_label='x', y_axis_label='y'
)
p.line(X, Y, legend_label="Przybliżanie sie do Pi", line_width=2)
p.line(X, Z, legend_label="Pi = 3.14.", line_width=2, line_color="red")
# show the results
show(p)

