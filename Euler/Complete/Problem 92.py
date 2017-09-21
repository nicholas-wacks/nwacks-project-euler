chain89Results = set()
chain89Results.add(89)

chain1Results = set()
chain1Results.add(1)

def sumOfDigitsSquared(n):
    temp = 0
    for digit in str(n):
        temp += int(digit) ** 2
    return temp

for i in range(2, 10000000):
    temp = i
    affectedNums = set()
    affectedNums.add(i)

    while (temp not in chain1Results and temp not in chain89Results):
        temp = sumOfDigitsSquared(temp)
        affectedNums.add(temp)

    if temp in chain1Results:
        chain1Results.update(affectedNums)
    else:
        chain89Results.update(affectedNums)

print(chain89Results)
print(len(chain89Results))

