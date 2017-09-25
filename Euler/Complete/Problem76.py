#How many different ways can one hundred be written as a sum of at least two positive integers?

foundAnswers = {}

def getCountOfSumsByMaxNumberAndTotalValue(maxNum, totalLeft):
    if (maxNum == 1 or totalLeft <= 1):
        return 1

    if ((maxNum, totalLeft) in foundAnswers):
        return foundAnswers[(maxNum, totalLeft)]

    count = 0
    for i in range(1, min(maxNum + 1, totalLeft + 1)):
        count += getCountOfSumsByMaxNumberAndTotalValue(i, totalLeft - i)
        
    foundAnswers[(maxNum, totalLeft)] = count
    return count

sumCount = 0
totalValue = 100
for i in range(totalValue - 1, 0, -1):
    sumCount += getCountOfSumsByMaxNumberAndTotalValue(i, totalValue - i)
    print(sumCount)