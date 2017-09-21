import math

values = [100, 50, 20, 10, 5, 2, 1]

def getCombinations(minVal, remainder):
    if (minVal == len(values) - 1 or remainder == 0):
        return 1
    sum = 0
    for i in range(math.floor(remainder / values[minVal]) + 1):
        sum += getCombinations(minVal + 1, remainder - values[minVal] * i)

    return sum

print (1 + getCombinations(0, 200))
