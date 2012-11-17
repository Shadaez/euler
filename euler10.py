"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import math
def primeCheck():
    p = 2
    x = 0
    n = 3
    while n <= 2000000:
        x = int(math.ceil(n**.5))
        for i in range(2, x + 1):
            if n%i == 0:
                break
        else:
            p += n
        n += 1
    else:
        print n
        print p
primeCheck()
