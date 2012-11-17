#Euler 4
#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome(z):
    length = len(z) - 1
    if z[0] == z[length]:
        if length <= 1:
            return True
        else:
            z.pop(length)
            z.pop(0)
            return (True and palindrome(z))
    else:
        return False
def breakApart(z):
    p = []
    if z >= 10:
        p = [z%10] + breakApart(z/10)
        return p
    else:
        return [z]
r = 100
t = 100
q = r*t
largestPalindrome = 0

while r < 1000:
    r += 1
    while t < 1000:
        t += 1
        q = r*t
        if palindrome(breakApart(q)) and q > largestPalindrome:
            print palindrome(breakApart(q))
            print q
            largestPalindrome = q
    else:
        t = 100
else:
    print largestPalindrome

