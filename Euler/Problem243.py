#R(d) < 15499/94744
import math
from fractions import gcd


class prime:
    primes = [2, 3]

    def getNthPrime(self, n):
        if (len(self.primes) >= n):
            return self.primes[n - 1]

        self.fillPrimesBelow(self.primes[len(self.primes) - 1] * 4)
        return self.primes[n - 1]

    def fillPrimesBelow(self, n):
        i = math.floor(self.primes[len(self.primes) - 1] / 6) * 6 + 5
        while (self.primes[len(self.primes) - 1] < n):
            if (self.isPrime(i)): 
                self.primes.append(i)
            if (self.isPrime(i + 2)):
                self.primes.append(i + 2)
            i += 6

    def isPrime(self, n):
        if (n <= self.primes[-1]):
            return (n in self.primes)
        
        i = 0
        while (self.primes[i] * self.primes[i] <= n):
            if (n % self.primes[i] == 0):
                return False
            i += 1
        return True

    def outerIsPrime(self, n):
        if (n > self.primes[-1]):
            self.fillPrimesBelow(n + 2)
        return (n in self.primes)

def getRofD(d):
    count = 0

    for i in range(1, d):
        if gcd(i, d) == 1:
            count += 1

    return count / (d - 1)

p = prime()
rLine = 15499/94744
i = 1

print(getRofD(12))

t = 1

while getRofD(t * p.getNthPrime(i)) >= rLine:
    i += 1
    t *= p.getNthPrime(i)
    if (i % 10 == 0):
        print (str(i) + ': ' + str(t))

print(t * p.getNthPrime(i))