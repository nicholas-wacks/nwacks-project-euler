import math

def getSumProblemOne(n):
    sum = 0
    sum += 3 * math.floor(getSeriesSum(n / 3))
    sum += 5 * math.floor(getSeriesSum(n / 5))
    sum -= 15 * math.floor(getSeriesSum(n / 15))
    return sum

def getSeriesSum(n):
    n = math.floor(n)
    return n * (n + 1) / 2

print(getSumProblemOne(999))