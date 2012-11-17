"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage."""
#one, two, three, four, five, six, seven, eight, nine, ten, eleven,
#twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen,
#nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,
import math
x = 1
y = 0
p = 0
q = 0
count = 0
def fart(z):
    fart = 0
    y = z
    if y == 1 or y == 2 or y == 6:
        fart += 3
    elif y == 3 or y == 7 or y == 8:
        fart += 5
    elif y == 4 or y == 5 or y == 9:
        fart += 4
    return fart
while x <= 1000:
    y = x
    if x == 1000:
        count += 11
        print count
        break
    while True:
        y = x % 10
        if not (((math.floor(x/10)%10)*10+x%10) >= 10 and ((math.floor(x/10)%10)*10+x%10) < 20): 
                count += fart(y)
                
        if x >= 10:
            if (((math.floor(x/10)%10)*10+x%10) >= 10 and ((math.floor(x/10)%10)*10+x%10) < 20):
                y = int((math.floor(x/10)%10)*10 + x%10)
                if y == 10: # 10 ten
                    count += 3
                elif y == 13 or y == 14: #thirteen fourteen eighteen nineteen
                    count += 8
                elif y == 18 or y == 19:
                    count += 8
                elif y == 12 or y == 11: # twelve eleven
                    count += 6
                elif y == 15 or y == 16: # fifteen sixteen
                    count += 7
                elif y == 17: # seventeen
                    count += 9
            else: # 20-99 twenty:6 thirty:6 forty5 fifty5 sixty5 seventy7 eighty6 ninety6
                y = math.floor(x/10)%10
                if y == 5 or y == 6 or y == 4:
                    count += 5
                elif y == 7:
                    count += 7
                elif y == 2 or y == 3 or y == 8 or y == 9:
                    count += 6
        if x >= 100:
            y = (math.floor(x/100)%10)
            count += 7
            count += fart(y)
            if not (x%10 == 0 and math.floor(x/10) % 10 == 0):
                count += 3
        break
    print x, count, p, q, (math.floor(x/10)%10)*10+x%10
    x += 1
print count

