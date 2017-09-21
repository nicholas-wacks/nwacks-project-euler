import math

class amicable:
    sumOfDivs = dict()
    sumOfDivs[1] = 1

    def getSumOfAmicable(self, n):
        sum = 0
        for i in range(1, n):
            recip = self.getSumOfDivisors(i)
            if (i == self.getSumOfDivisors(recip) and recip != i):
                sum += i
                print(str(i) + ',' + str(recip))
        return sum

    def getSumOfDivisors(self, n):
        if (n in self.sumOfDivs):
            return self.sumOfDivs[n]

        sum = 0
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if (n % i == 0 and i < n):
                sum += i
                if (i != 1 and i * i != n):
                    sum += n / i

        self.sumOfDivs[n] = sum
        return sum

a = amicable()
print(a.getSumOfAmicable(10000))