#prime numbers to 100
def prime(n):
   is_prime = True
   if n == 1:
       return False
   else:
       for i in range(2, (int)(n//2)+1):
           if n % i == 0:
               is_prime = False
               break
       return is_prime        


for i in range(1, 100):
   if prime(i):
       print(i, end=" ")     #in one line: print(i, end=" ")