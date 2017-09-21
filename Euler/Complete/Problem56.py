def getDigitalSum(n):
    sum = 0
    for s in str(n):
        sum += int(s)
    return sum

max = 0

for a in range(1, 100):
    for b in range(1, 100):
        d = getDigitalSum(a ** b)
        if (d > max):
            max = d

print (max)