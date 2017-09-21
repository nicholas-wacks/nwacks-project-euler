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

    def isTruncatablePrime(self, n):
        t = n
        while (t >= 1):
            if (t in self.primes):
                t = math.floor(t / 10)
            else:
                return False

        t = n
        while (t >= 1):
            if (t in self.primes):
                t = t % (10 ** math.floor(math.log10(t)))
            else:
                return False

        return True

p = prime()
p.fillPrimesBelow(1000000)
count = 0
sum = 0
i = 4
while (count < 11 and i < len(p.primes)):
    if (p.isTruncatablePrime(p.primes[i])):
        count += 1
        sum += p.primes[i]
        print(p.primes[i])
    i += 1

print(count)
print(sum)