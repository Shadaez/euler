#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?
strDigit = 2**1000
x = []
z = 0
y = 0
def breakApart(z):
    p = []
    if z >= 10:
        p = [z%10] + breakApart(int(z)/10)
        return p
    else:
        return [int(z)]
x = breakApart(strDigit)
while z < len(x):
    y+=x[z]
    z+=1
print y 
