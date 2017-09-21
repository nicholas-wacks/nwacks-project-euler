import time

#TODO: refactor for time

evens = ['2', '4', '6', '8', '0']

def isReversible(n):
    if n % 10 == 0:
        return False

    temp = str(n + int(str(n)[::-1]))

    if any(even in temp for even in evens):
        return False
    return True


count = 0

start = time.time()

for i in range(11, 1000000000, 2):
    t = i

    if (int(str(i)[0]) % 2 == 1):
        t += 1

    if (isReversible(t)):
        count += 1

    if (i % 1000001 == 0):
        print(str(i - 1) + ": " + str(time.time() - start) + "s")

print(count)