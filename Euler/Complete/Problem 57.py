import math

numer = 3
denom = 2
count = 0

for i in range(1000):
    numer += denom
    t = denom
    denom = numer
    numer = t + denom
    if (math.floor(math.log10(numer)) > math.floor(math.log10(denom))):
        count += 1
    if (i % 100 == 0):
        print (i)

print (count)