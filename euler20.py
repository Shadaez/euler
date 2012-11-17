"""n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""
import math
x = 1
n = 1
def fart(y):
    h = ''
    h = str(y)
    z = 0
    for i in range(len(h)):
        z += int(h[i:i+1])
    return z
while n <= 100:
    x *= n
    n += 1
print fart(x)
