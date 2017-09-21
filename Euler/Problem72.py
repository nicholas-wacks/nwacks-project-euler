import gmpy2

def validFractionsWithN(n, maxD):
    if n == 1:
        return maxD - 1
    return n



count = 0

#for d in range(2, 1000001):
#    for n in range(1, d):
#        if (int(gmpy2.gcd(n, d)) == 1):
#            count += 1
#    if (d % 10000 == 0):
#        print(str(n) + ': ' + str(count))

for n in range(2, 1000001):
    count += validFractionsWithN(n, 1000000)

print(count)