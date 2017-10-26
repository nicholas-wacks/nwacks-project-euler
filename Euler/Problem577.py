solutions = {}

sum = 0

def getHofN(n):
    if n < 0:
        return 0

    if n in solutions:
        return solutions[n]

    val = 0

    innerN = n - 3
    val += (innerN + 1) * (innerN + 2) / 2

    if (n >= 6):
        val += getHofN(n - 3)

    solutions[n] = val
    return val

print(getHofN(3))
print(getHofN(6))
print(getHofN(20))

#for n in range(3, 12346):
#    sum += getHofN(n)

print(sum)