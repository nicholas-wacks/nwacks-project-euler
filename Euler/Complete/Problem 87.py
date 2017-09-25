#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

import math

topNumber = 50000000
maxSquare = math.floor(topNumber ** (1/2))
maxCube = math.floor(topNumber ** (1/3))
maxFourth = math.floor(topNumber ** (1/4))

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

p = prime()
p.fillPrimesBelow(maxSquare + 1)

numbersFound = set()

for i in p.primes:
    if (i <= maxSquare):
        for j in p.primes:
            if (j <= maxCube):
                for k in p.primes:
                    if (i**2 + j**3 + k**4) >= topNumber:
                        break

                    if (k <= maxFourth):
                        numbersFound.add(i**2 + j**3 + k**4)

print(len(numbersFound))