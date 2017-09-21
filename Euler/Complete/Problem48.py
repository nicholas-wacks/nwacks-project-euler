sum = 0

for i in range(1, 1001):
    sum += (i ** i) % 10000000000
    sum = sum % 10000000000

print (sum)