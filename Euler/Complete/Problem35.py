import math
from itertools import permutations

class prime:
    primes = [2, 3]

    def getNthPrime(self, n):
        if (len(self.primes) >= n):
            return self.primes[n - 1]

        self.fillPrimes(n)
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
        i = 0
        while (self.primes[i] * self.primes[i] <= n):
            if (n % self.primes[i] == 0):
                return False
            i += 1
        return True

count = 0
p = prime()
p.fillPrimesBelow(1000000)
for i in range(2, 1000000):
    if (not '0' in str(i)):
        valid = True
        for l in range(len(str(i))):
            s = str(i)[l:] + str(i)[0:l]
            if (not int("".join(s)) in p.primes):
                valid = False
                break;
        if (valid):
            count += 1
    if (i % 1000 == 0):
        print(i)

print(count)

