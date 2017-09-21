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
p.fillPrimesBelow(500000)

max = 0
index = 0
for a in range(-999, 1000):
    for b in range(-a + 1, 1001):
        i = 0
        while (((i ** 2) + (a * i) + b) in p.primes or ((i ** 2) + (a * i) + b) > p.primes[len(p.primes) - 1]):
            if (((i ** 2) + (a * i) + b) > p.primes[len(p.primes) - 1]):
                p.fillPrimesBelow((i ** 2) + (a * i) + b + 1)
            i += 1
        if (i > max):
            index = a * b
            max = i

    if (a % 10 == 0):
        print(str(max) + ' ' + str(a))
print(index)
