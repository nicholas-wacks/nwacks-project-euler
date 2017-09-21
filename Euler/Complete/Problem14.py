class sequences:
    lengths = dict()
    lengths[1] = 1

    def getLongestUnder(self, n):
        max = 1
        number = 1
        for i in range(2, n):
            sLength = self.getLength(i)
            if (sLength > max):
                max = sLength
                number = i
        print (str(number) + ' ' + str(max))
        return number

    def getLength(self, i):
        if (i in self.lengths):
            return self.lengths[i]

        v = 1 + self.getLength(self.nextElement(i))
        self.lengths[i] = v
        return v

    def nextElement(self, i):
        if (i % 2 == 0):
            return i / 2
        return 3 * i + 1

s = sequences()
print (s.getLongestUnder(14))
print (s.getLongestUnder(1000000))