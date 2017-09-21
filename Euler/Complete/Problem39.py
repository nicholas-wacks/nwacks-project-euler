import math

max = 0
maxP = 0

for p in range(4, 1001):
    tCount = 0
    for a in range(1, math.ceil(p / 2)):
        for b in range(a, math.ceil(p / 2)):
            c = math.sqrt((a ** 2) + (b ** 2))
            if (a + b + c > p):
                break
            if (not c.is_integer()):
                continue
            if (a + b + c == p):
                tCount += 1
                break
    if (tCount > max):
        max = tCount
        maxP = p
        print(p)

print(maxP)