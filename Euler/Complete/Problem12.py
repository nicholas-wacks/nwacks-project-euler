import math

def firstTriangleWithNDivisors(n):
    i = 1
    divisors = 0
    while (divisors <= n):
        divisors = 0
        val = i * (i + 1) / 2
        for j in range(1, math.ceil(math.sqrt(val)) + 1):
            if (val % j == 0):
                divisors += 1
                if (j * j < val):
                    divisors += 1
        i += 1
    return val

print (firstTriangleWithNDivisors(5))
print (firstTriangleWithNDivisors(500))