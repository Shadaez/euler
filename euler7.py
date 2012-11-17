import math
"""By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13."""

#What is the 10 001st prime number?
def primeCheck():
    p = 0
    x = 0
    n = 1
    while True:
        x = int(math.ceil(n**.5))
        for i in range(2, x + 1):
            if n%i == 0:
                break
        else:
            p += 1
            if p == 10001:
                print n
        n += 1
                
primeCheck()
