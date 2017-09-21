import math

class abundant:
    abundantNumbers = []

    def getSumOfInexpressible(self, n):
        sum = 0
        for i in range(1, n):
            val = self.getSumOfDivisors(i)
            if (val > i):
                self.abundantNumbers.append(i)

            if (not self.canBeSumOfAbundants(i)):
                sum += i
        return sum

    def getSumOfDivisors(self, n):
        sum = 0
        sq = math.sqrt(n)
        for i in range(1, math.ceil(sq)):
            if (n % i == 0 and i < n):
                sum += i
                if (i != 1):
                    sum += n / i
        if (sq.is_integer()):
            sum += sq

        return sum

    def canBeSumOfAbundants(self, n):
        i = 0
        j = len(self.abundantNumbers) - 1
        while (i <= j):
            if (self.abundantNumbers[i] + self.abundantNumbers[j] == n):
                return True
            if (self.abundantNumbers[i] + self.abundantNumbers[j] < n):
                i += 1
            else:
                j -= 1
        return False
        

a = abundant()
print (a.getSumOfInexpressible(28123))