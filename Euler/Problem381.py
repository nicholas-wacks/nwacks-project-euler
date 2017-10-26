#For a prime p let S(p) = (sum((p-k)!)) mod(p) for 1 <= k <= 5.

#For example, if p=7,
#(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
#As 872 mod(7) = 4, S(7) = 4.

#It can be verified that sum(S(p)) = 480 for 5 <= p < 100.

#Find sum(S(p)) for 5 <= p < 10^8.

#(x - 1)! mod x == -1 (x - 1)
#(x - 2)! mod x == (x - 1) / (x - 1) == 1
#(x - 3)! mod x == 1 / (x - 2) 
#   -> r * (x - 2) == (n * x) + 1

import primesieve, math


class solver:
    def __init__(self):
        self.primePoint = 1
        self.currentFactorialTop = 1

    def sOfP(self, p):
        for i in range(self.currentFactorialTop + 1, p - 4):
            self.primePoint *= i
            self.currentFactorialTop = i

        retVal = 0
        tempFactorial = self.currentFactorialTop
        for i in range(1,6):
            retVal += tempFactorial
            tempFactorial *= (p - 5 + i)
        return retVal % p

print(primesieve.count_primes(10**8))

iterator = primesieve.Iterator()
prime = iterator.next_prime()
prime = iterator.next_prime()
prime = iterator.next_prime()

count = 0
topPoint = 10 ** 8
s = solver()
while prime < topPoint:
    temp = s.sOfP(prime)
    count += temp
    #print (str(prime) + ': ' + str(temp) + ', ' + str(count) + '; ' + str(s.currentFactorialTop) + '! = ' + str(s.primePoint))
    prime = iterator.next_prime()

print(count)