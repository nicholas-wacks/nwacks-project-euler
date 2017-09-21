val = ''
i = 1
while (len(val) < 1000000):
    val += str(i)
    i += 1

p = 1
product = 1
while (p <= 1000000):
    product *= int(val[p - 1])
    p *= 10

print(product)