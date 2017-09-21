

def getNdivPhi(n):
    phi = 1

    for i in range(2, n):
        if (n % i != 0):
            phi += 1

    return n / phi

maxVal = 0
nAtMaxVal = 0

for i in range(0, 1000000, 2):
    temp = getNdivPhi(i)
    if (temp > maxVal):
        maxVal = temp
        nAtMaxVal = i

    if (i % 10000 == 0):
        print(str(i) + ": " + str(temp))

print(i)