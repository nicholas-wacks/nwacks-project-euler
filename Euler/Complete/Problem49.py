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
p.fillPrimesBelow(10000)

for i in range(1001, 3341):
    if (p.isPrime(i) and p.isPrime(i + 3330) and p.isPrime(i + 6660)
        and sorted(str(i)) == sorted(str(i + 3330)) and sorted(str(i)) == sorted(str(i + 6660))):
        print(i)