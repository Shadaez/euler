i = [1, 2]
x = 0
while x <= 4000000:
    lenI = len(i)
    i.append(i[lenI-1] + i[lenI-2])
    x = i[lenI]
else:
    i.pop(len(i)-1)
    y = 0
    while y < len(i):
        if (i[y]%10)%2 != 0:
            i.pop(y)
        else:
            y += 1
    print sum(i)
