import math
from itertools import permutations

def isPrime(n):
    v = int(n)
    if (v % 2 == 0 or v % 3 == 0):
        return False

    for i in range(6, math.ceil(math.sqrt(v)), 6):
        if (v % (i - 1) == 0 or v % (i + 1) == 0):
            return False
    return True

def getPrimePerm(s):
    l = getXStringList(s)
    
    for baseOption in l:
        primes = 0
        firstPrime = ""
        for i in range(10):
            if (i != 0 or baseOption[0] != 'X'):
                if (isPrime(int(baseOption.replace('X', str(i))))):
                    primes += 1
                    if (firstPrime == ""):
                        firstPrime = baseOption.replace('X', str(i))
                if (10 - i + primes < 8):
                    break
        if (primes >= 8):
            return firstPrime
    return ""

def getXStringList(s):
    if ("N" not in s):
        return set([s])
    else:
        l = []
        getXStringRecursive(s, l)
        return set(l)

def getXStringRecursive(s, l):
    if ("N" not in s):
        l.append(s)
    else:
        for i in range(10):
            getXStringRecursive(s.replace('N', str(i), 1), l)

baseStr = "X"
done = False

while (not done):
    while ("XX" in baseStr):
        for lastDigit in range(1, 10, 2):
            for perm in set(permutations(baseStr)):
                st = "".join(perm)
                s = getPrimePerm(st + str(lastDigit))
                #print(str(firstDigit) + st + str(lastDigit))
                if (s != ""):
                    print(s)
                    done = True
        baseStr = baseStr.replace('X', 'N', 1)
        print(baseStr)
    baseStr = baseStr.replace('N', 'X')
    baseStr += "X"
