
sum = 0
for i in range(11, 999999):
    tempSum = 0
    for s in str(i):
        tempSum += int(s) ** 5
    if (tempSum == i):
        sum += i
        print(i)

print(sum)