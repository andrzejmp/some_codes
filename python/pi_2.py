#number_pi_2
#Calculating number Pi, version 2

number = 3.14159

def pi2(number, error):
    s = 0
    i = 1
    while abs(number-s)>error:
        s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
        i+=1
    return error, s, i

print ('%10s %20s %10s' % pi2(number, 0.1))
print ('%10s %20s %10s' % pi2(number, 0.01))
print ('%10s %20s %10s' % pi2(number, 0.001))
print ('%10s %20s %10s' % pi2(number, 0.0001))
print ('%10f %20s %10s' % pi2(number, 0.00001))
print ('%10f %20s %10s' % pi2(number, 0.000001))