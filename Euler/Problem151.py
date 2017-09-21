def getAddition(n):
    if n == 1:
        return tuple([])
    if n == 2:
        return tuple([1])
    if n == 4:
        return tuple([1, 2])
    if n == 8:
        return tuple([1, 2, 4])
    if n == 16:
        return tuple([1, 2, 4, 8])


def getNextSteps(st, num):
    retVal = {}

    for i in range(len(st)):
        addition = getAddition(st[i])
        t = tuple(sorted(st[0:i] + st[i+1:len(st)] + addition))
        
        if t in retVal:
            retVal[t] += num
        else:
            retVal[t] = num

    return retVal

startingSet = {(16,): 1}
count = 0

for i in range(16):
    nextSet = {}

    tempCount = 0
    for st in startingSet.keys():
        if (len(st) == 1):
            tempCount += startingSet[st]

        if (st != (1)):
            t = getNextSteps(st, startingSet[st])
        
            for step in t:
                if step in nextSet:
                    nextSet[step] += t[step]
                else:
                    nextSet[step] = t[step]

    count += tempCount / sum(startingSet.values())

    startingSet = nextSet
    print(count)

print(count - 2)