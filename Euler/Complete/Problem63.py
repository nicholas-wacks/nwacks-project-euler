import math

count = 0

for i in range(1, 100):
    for j in range(1, 10):
        if (math.floor(math.log10(j ** i)) + 1 == i):
            print (str(j) + "^" + str(i) + ": " + str(j**i))
            count += 1
print (count)