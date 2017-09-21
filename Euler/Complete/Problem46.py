import math

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
p.fillPrimesBelow(50000)

i = 35
done = False
while (not done):
    val = False
    if (i > p.primes[len(p.primes) - 1]):
        p.fillPrimesBelow(i + 1000)

    for j in p.primes:
        if (j > i):
            break
        if (math.sqrt((i - j) / 2).is_integer()):
            val = True
            break

    if (not val):
        print (i)
        done = True

    if (i % 1000 == 1):
        print (i)
    i += 2