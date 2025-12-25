def gcd(m,n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
        
m = 99
n = 132
print(gcd(m,n))