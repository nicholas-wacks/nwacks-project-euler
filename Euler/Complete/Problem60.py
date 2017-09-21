import math

class prime:
    primes = [2, 3]

    def getNthPrime(self, n):
        if (len(self.primes) >= n):
            return self.primes[n - 1]

        self.fillPrimesBelow(n)
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

concatPrimes = dict()
def isConcatPrime(a, b, pr):
    if ((a, b) in concatPrimes):
        return concatPrimes[(a, b)]

    c1 = int(str(pr.primes[a]) + str(pr.primes[b]))
    c2 = int(str(pr.primes[b]) + str(pr.primes[a]))
    result = (pr.outerIsPrime(c1) and pr.outerIsPrime(c2))
    concatPrimes[(a, b)] = result
    return result

p = prime()
p.fillPrimesBelow(15000)
done = False
a = 5

while (not done):
    for b in range(1, a):
        if (isConcatPrime(a, b, p)):
            for c in range(1, b):
                if (isConcatPrime(a, c, p) and isConcatPrime(b, c, p)):
                    for d in range(1, c):
                        if (isConcatPrime(a, d, p) and isConcatPrime(b, d, p) and isConcatPrime(c, d, p)):
                            for e in range(1, d):
                                if (isConcatPrime(a, e, p) and isConcatPrime(b, e, p) and isConcatPrime(c, e, p) and isConcatPrime(d, e, p)):
                                    keys = [a, b, c, d, e]
                                    done = True
                                    s = 0
                                    for k in keys:
                                        s += p.primes[k]
                                        print (str(k) + ' ' + str(p.primes[k]))
                                    print (s)
    a += 1
    if (a % 20 == 0):
        print (a)