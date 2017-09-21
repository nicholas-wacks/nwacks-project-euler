import math, gmpy2
from decimal import *

dAtMaxVal = 0
maxVal = -1

for i in range(2, 1000):
    if (gmpy2.is_square(i)):
        continue

    lim = math.floor(math.sqrt(i))

    m = 0
    d = 1
    a = lim



#x^2 - Dy^2 = 1 for smallest x
#y = sqrt((x^2 - 1) / D)
#x^2 - 1 = N*D [N is psitive perfect square]
#x = sqrt(ND + 1)

#x^2 = Dy^2 + 1

# x > 718

#def getAvals(n):
#    aVals = list()

#    d = math.sqrt(n)
#    a0 = math.floor(d)
#    b0 = a0
#    c0 = n - (a0**2)
#    aVals.append(a0)

#    a = math.floor((a0 + b0) / c0)
#    b = a * c0 - b0
#    c = (n - b**2) / c0

#    while (b != b0 or c != c0):
#        aVals.append(a)
#        a = math.floor((a0 + b) / c)
#        b = a * c - b
#        c = math.floor((n - b**2) / c)

#    return aVals

#def getNDfromPeriod(aVals):
#    aVals.reverse()

#    n = Decimal(1)
#    d = Decimal(aVals[0])

#    for i in range(1, len(aVals) - 1):
#        temp = Decimal(n + ((aVals[i]) * d))
#        n = Decimal(d)
#        d = Decimal(temp)
    
#    n += aVals[len(aVals) - 1] * d

#    return (n, d)

#def getNDfromD(d):
#    aVals = getAvals(d)

#    return getNDfromPeriod(aVals)

#maxVal = 0
#dAtMaxVal = -1

#dVals = list(range(2, 1001))
#for i in range(2, 32):
#    dVals.remove(i**2)

#for d in dVals:
#    x = getNDfromD(d)[0]

#    if (x > maxVal):
#        maxVal = x
#        dAtMaxVal = d

#print (dAtMaxVal)