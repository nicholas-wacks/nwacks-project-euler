import math

def nChooseR(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

print (nChooseR(23, 10))

count = 0
for i in range(23, 101):
    for j in range(2, i - 1):
        if (nChooseR(i, j) > 1000000):
            count += 1
print (count)