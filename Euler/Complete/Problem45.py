import math

def nthHexagon(n):
    return (n * (2 * n - 1))

def isPentagon(n):
    return ((math.sqrt(1 + 24 * n) + 1) / 6).is_integer()

def isTriangle(n):
    return ((math.sqrt(1 + 8 * n) - 1) / 2).is_integer()

print(isTriangle(10))
print(isTriangle(15))
print(isTriangle(18))
i = 144
incomplete = True
while (incomplete):
    n = nthHexagon(i)
    if (isPentagon(n) and isTriangle(n)):
        print(n)
        incomplete = False
    i += 1
    if (i % 100 == 0):
        print(i)