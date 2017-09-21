import math

def isPrime(n):
    v = int(n)
    if (v % 2 == 0 or v % 3 == 0):
        return False

    for i in range(5, math.ceil(math.sqrt(v)) + 6, 6):
        if (v % (i) == 0 or v % (i + 2) == 0):
            return False
    return True

row = 2
primes = 3
corners = 1
current = 9
done = False
goal = .1

while (not done):
    row += 2
    for i in range(4):
        current += row
        if (isPrime(current)):
            primes += 1

    if (primes / (2 * row + 1) < goal):
        done = True

    if (row % 100 == 0 or row < 8):
        print (str(primes) + "/" + str(2 * row + 1))

print(row + 1)