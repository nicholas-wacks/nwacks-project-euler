import gmpy2
from decimal import *

getcontext().prec = 500

limit = 99
aVals = list()

for i in range(limit):
    if (i % 3 == 1):
        aVals.append(Decimal(2 * (i + 2) / 3))
    else:
        aVals.append(Decimal(1))
        
aVals.reverse()

n = Decimal(1)
d = Decimal(aVals[0])

for i in range(1, limit):
    temp = Decimal(n + ((aVals[i]) * d))
    n = Decimal(d)
    d = Decimal(temp)
    

n += 2 * d

print (str(n) + "/" + str(d))

sum = 0
for s in str(int(n)):
    sum += int(s)

print(sum)