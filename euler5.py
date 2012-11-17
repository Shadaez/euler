#Euler 2520 is the smallest number that can be divided by each
#of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly
#divisible by all of the numbers from 1 to 20?

#this sucks and is slow, i need to find GCD and implement them to get the answer quicker
def primeCheck(n):
    primeList = []
    x = 0
    while n >= 1:
        #if it's even it's not prime
        #start checking if it's
        x = int(n**.5)
        if n%2 != 0:
            if n%10 == 5:
                n -= 2
            while x > 1:
                if n%x == 0:
                    break
                x -= 1
            else:
                primeList.append(n)
        n -= 1
    else:
        return primeList
x = 1
y = 20
found = False
primeList = primeCheck(y)
print primeList
while not found:
    x += 1
    for i in primeList:
        if x%i != 0:
                break
    else:
        for z in range(3, y+1):
            if x%z != 0:
                break
        else:
            print "found it"
            print x





