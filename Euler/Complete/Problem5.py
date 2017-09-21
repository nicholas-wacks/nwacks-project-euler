def getSmallestMultiple(n):
    factors = dict()
    for i in range(1, n + 1):
        tempFactors = dict()
        tempVal = i
        index = 3

        while (tempVal % 2 == 0):
            tempVal /= 2
            if (2 in tempFactors):
                tempFactors[2] += 1
            else:
                tempFactors[2] = 1

        while (index <= tempVal):
            if (tempVal % index == 0):
                tempVal /= index
                if (index in tempFactors):
                    tempFactors[index] += 1
                else:
                    tempFactors[index] = 1
            else:
                index += 2
        for k in tempFactors:
            if ((k in factors and tempFactors[k] > factors[k]) or k not in factors):
                factors[k] = tempFactors[k]
    
    val = 1
    for k in factors:
        for i in range(factors[k]):
            val *= k
    
    return val


print (getSmallestMultiple(10))
print (getSmallestMultiple(20))
