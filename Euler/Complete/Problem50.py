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
p.fillPrimesBelow(1000000)

max = 2
maxval = 5

for i in range(len(p.primes) - 1):
    for j in range(i, len(p.primes)):
        if (j - i > max):
            sum = 0
            for k in range(i, j + 1):
                sum += p.primes[k]
            if (sum >= 1000000):
                break;
            if (sum in p.primes):
                max = j - i + 1
                maxval = sum
                print (sum)

print (maxval)
print (max)