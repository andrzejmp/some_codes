def check_primes(n):
    is_prime = True
    n = int(n)
    for i in range(2, n // 2+1):    
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def get_edge(n):
    n = int(n)
    return n