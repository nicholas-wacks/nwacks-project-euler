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

base = "7654321"
while (len(base) > 0):
    for s in permutations(base):
        v = "".join(s)
        if (isPrime(int(v))):
            print(v)
            base = ""
            break
    print(base)
    base = base[1:]
