from decimal import *
import gmpy2

getcontext().prec = 102

sum = 0

for i in range(2, 100):
    if (gmpy2.is_square(i)):
        continue

    sq = Decimal(i).sqrt()
    st = str(sq)
    st = st[:-2]
        
    for s in st:
        if (s != '.'):
            sum += int(s)

print(sum)