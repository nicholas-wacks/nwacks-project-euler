import math, fractions
#not 4946
#not 7442

def getDistance(point1, point2):
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

count = 50 * 50 * 3

for x1 in range(1, 51):
    for y1 in range(1, 51):
        factor = fractions.gcd(x1, y1)
        count += math.floor(min(y1 * factor / x1, (50 - x1) * factor / y1)) * 2

print(count)