products = set()

for a in range(2, 9999):
    for b in range(a, 10000):
        c = a * b
        st = str(a) + str(b) + str(c)
        if (len(st) > 9):
            break
        s = ''.join(sorted(st))
        if (s == "123456789"):
            products.add(c)

sum = 0
for i in products:
    sum += i

print(sum)