#Let s(n) be the smallest number m such that n divides m!.
#So s(10)=5 and s(25)=10.
#Let S(n) be ?s(i) for 2 ? i ? n.
#S(100)=2012.

#Find S(10^8).

#10^8 = 5^8 * 2^8
import math
from functools import reduce

twoFactors = 0
neededTwoFactors = 0
fiveFactors = 0
neededFiveFactors = 2

def factors(n):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#i = 1
#while (twoFactors < neededTwoFactors or fiveFactors < neededFiveFactors):
#    i += 1
#    temp = i
#    while (temp % 2 == 0):
#        temp /= 2
#        twoFactors += 1

#    while (temp % 5 == 0):
#        temp /= 5
#        fiveFactors += 1

for i in range(2, 100000001):
    temp = factors(i)
    if (i % 10000000 == 0):
        print(temp)