import math, gmpy2

def getFactorCount(n):
    count = 0

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if (n % i == 0):
            count += 2

    if (gmpy2.is_square(n)):
        count -= 1

    return count

count = 0
lastCount = getFactorCount(2)
for i in range(3, 10000000):
    temp = getFactorCount(i)
    if (temp == lastCount):
        count += 1

    lastCount = temp

    if (i % 100000 == 0):
        print(i)

print(count)