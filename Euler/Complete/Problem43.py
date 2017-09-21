from itertools import permutations

sum = 0
primes = [2,3,5,7,11,13,17]

for s in permutations("0123456789"):
    v = "".join(s)
    if (v[0] == '0'):
        continue

    valid = True
    for i in range(1, 8):
        if (int(v[i:i + 3]) % primes[i - 1] != 0):
            valid = False
            break

    if (valid):
        sum += int(v)
        print(v)

print(sum)