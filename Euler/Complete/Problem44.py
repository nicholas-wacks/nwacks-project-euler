import math

def nthPentagon(n):
    return (n * (3 * n - 1) / 2)

def isPentagon(n):
    return ((math.sqrt(1 + 24 * n) + 1) / 6).is_integer()

print (isPentagon(nthPentagon(5)))
print (isPentagon(17))

def getPentagon():
    i = 2
    while (i < 100000):
        n = nthPentagon(i)
        for j in range(i - 1, 0, -1):
            nj = nthPentagon(j)
            if (isPentagon(n + nj) and isPentagon(n - nj)):
                return [n, nj]
        i += 1
        if (i % 20 == 0):
            print(i)

p = getPentagon()
print(p)
print(p[0] - p[1])