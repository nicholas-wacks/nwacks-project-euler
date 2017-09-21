#n/d, n<d, d<= 1000000
import math, gmpy2

closestVal = 0
targetVal = 3/7
nums = [0, 0]

for d in range(2, 1000001):
    for n in range(math.floor(d * targetVal) - 1, d):
        if (n / d >= targetVal):
            break
        if (n / d > closestVal and gmpy2.gcd(n, d) == 1):
            closestVal = n / d
            nums = [n, d]
    if (d % 100000 == 0):
        print(nums)

print(nums)