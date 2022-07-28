
#ocalculating number pi

def pi1(n):
    s = 0
    for i in range(1,n+1):
        s = s + 1.0*(-1)**(i+1)*4/(2*i-1)
    return s

print (pi1(10))
print (pi1(20))
print (pi1(30))

print (pi1(1000000))