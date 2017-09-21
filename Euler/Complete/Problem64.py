import math

nVals = list(range(2, 10000))
for i in range(2, 100):
    nVals.remove(i**2)

count = 0

def isOddPeriodRoot(n):
    d = math.sqrt(n)
    a0 = math.floor(d)
    b0 = a0
    c0 = n - (a0**2)

    a = math.floor((a0 + b0) / c0)
    b = a * c0 - b0
    c = (n - b**2) / c0
    result = 1

    while (b != b0 or c != c0):
        result += 1
        a = math.floor((a0 + b) / c)
        b = a * c - b
        c = math.floor((n - b**2) / c)

    return result % 2 == 1

for n in nVals:
    if (isOddPeriodRoot(n)):
        count += 1

print(count)