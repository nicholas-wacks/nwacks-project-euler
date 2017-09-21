row = 2
sum = 1
current = 1

while (row <= 1000):
    for i in range(4):
        current += row
        sum += current
    row += 2
    if(row == 6):
        print(sum)

print(sum)