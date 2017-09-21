import math

def getNthPermutation(s, n):
    output = []
    l = len(s) - 1
    for i in range(len(s)):
        f = math.factorial(l)
        index = math.floor(n / f)
        n -= f * index
        l -= 1
        output.append(s[index])
        del s[index]
    return output

nums = [0,1,2,3,4,5,6,7,8,9]
print(getNthPermutation([0,1,2,3,4,5,6,7,8,9], 0))
print(getNthPermutation([0,1,2,3,4,5,6,7,8,9], 999999))
