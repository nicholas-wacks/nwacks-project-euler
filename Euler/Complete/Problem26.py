import math

def longestRepeatingSeries(n):
    max = 0
    for i in range(2, n):
        v = getRepeatingValue(i)
        if (v > max):
            max = i
    return max

def getRepeatingValue(n):
    values = [[0, 1]]
    current = 10
    while (current > 0):
        c = math.floor(current / n)
        m = current % n
        if ([c,m] in values):
            return len(values) - values.index([c, m])

        values.append([c, m])
        current = m * 10
    return 0

print(longestRepeatingSeries(10))
print(longestRepeatingSeries(1000))