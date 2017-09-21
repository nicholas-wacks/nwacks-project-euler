import math

chainLength = {}
chainLength[145] = 1

chainLength[169] = 3
chainLength[363601] = 3
chainLength[1454] = 3

chainLength[871] = 2
chainLength[45361] = 2

chainLength[872] = 2
chainLength[45362] = 2

def getChainLength(n):
    if (n in chainLength):
        return chainLength[n]

    temp = 0
    for s in str(n):
        temp += math.factorial(int(s))

    if (temp == n):
        chainLength[n] = 1
    else:
        length = getChainLength(temp)
        chainLength[n] = 1 + length
    return chainLength[n]

count = 0
for i in range(1, 1000000):
    if (getChainLength(i) == 60):
        count += 1

print(count)
