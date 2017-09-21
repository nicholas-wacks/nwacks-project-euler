import math
from itertools import permutations

i = 346
done = False
t = 0
goal = 5
digits = math.floor(math.log10(i ** 3))

sortedCubes = dict()

while (not done):
    t = ''.join(sorted(str(i ** 3)))
    
    if (t not in sortedCubes):
        sortedCubes[t] = [1, i ** 3]
    else:
        sortedCubes[t][0] += 1

    i += 1
    if (i % 100 == 0):
        print (i)

    if (math.floor(math.log10(i ** 3)) != digits):
        digits += 1
        minval = 0
        for s in sortedCubes.values():
            if (s[0] == goal):
                if (minval == 0 or s[1] < minval):
                    minval = s[1]
                done = True
        sortedCubes = dict()
        print(digits)
        if (done):
            print(minval)