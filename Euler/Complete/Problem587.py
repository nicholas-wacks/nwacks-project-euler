import math

totalArea = 1 - (math.pi / 4)
factor = 1 - 0.001

def getTotalArea(n):
    x = (1 - n + math.sqrt(2 * (n ** 3))) / ((n ** 2) + 1)
    
    top = ((1 / (2 * n)) - (1 / n) + 1) - (((x ** 2) / (2 * n)) - (x / n) + x)
    bottom = (math.pi / 4) - ((math.asin(x) / 2) + ((x / 2) * math.sqrt(1 - (x ** 2))))

    return top - bottom

n = 1
while (getTotalArea(n) < totalArea * factor):
    print(str(n) + ": " + str(getTotalArea(n)) + ": " + str(getTotalArea(n) / totalArea))
    n += 1

print(str(n) + ": " + str(getTotalArea(n)) + ": " + str(getTotalArea(n) / totalArea))
print (n)