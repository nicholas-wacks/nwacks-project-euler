import math

sum = 0

for i in range(10, 2540160):
    tSum = 0
    for s in str(i):
        tSum += math.factorial(int(s))
    if (tSum == i):
        sum += i
    if (i % 10000 == 0):
        print(i)

print(sum)