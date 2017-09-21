import gmpy2, math

count = 0

for d in range(4, 12001):
    for n in range(math.ceil(d / 3), math.floor(d / 2) + 1):
        if (n / d > 1 / 3 and n / d < 1 / 2 and gmpy2.gcd(n, d) == 1):
            count += 1

    if (d % 1000 == 0):
        print(count)

print(count)
