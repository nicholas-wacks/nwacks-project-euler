numer = 1
denom = 1

for r in range(1, 10):
    for a in range(1, 10):
        for b in range(a + 1, 10):
            if ((a + r * 10) / (b + r * 10) == a / b):
                numer *= a
                denom *= b
            if ((a * 10 + r) / (b + r * 10) == a / b):
                numer *= a
                denom *= b
            if ((a + r * 10) / (b * 10 + r) == a / b):
                numer *= a
                denom *= b
            if ((a * 10 + r) / (b * 10 + r) == a / b):
                numer *= a
                denom *= b

print(str(numer) + '/' + str(denom))