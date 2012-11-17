n = 600851475143
factors = []
def poop(p):
    y = []
    x = 1
    while x < p**.5:
        if p%x == 0:
            y.append(x) 
        x += 1
    return y
def isPrime(o):
    x = 2
    while x <= o**.5:
        if o%x == 0:
            return False
        x += 1
    else:
        return True
factors = poop(n)
print factors
print len(factors)
while not isPrime(factors[len(factors)-1]):
    print factors[len(factors)-1]
    factors.pop(len(factors)-1)
else:
    print factors
