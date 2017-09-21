def getPrimeFactors(n):
    factors = set()
    i = 3

    while (n % 2 == 0 and n >= 2):
        n /= 2
        factors.add(2)

    while (n > 1):
        if (i * i >= n):
            factors.add(n)
            n = 1
        elif (n % i == 0):
            n /= i
            factors.add(i)
        else:
            i += 2
    return factors

series = 0
seriesStart = -1
i = 33400

while (series < 4):
    if (len(getPrimeFactors(i)) == 4):
        if (series != 0):
            series += 1
        else:
            series = 1
            seriesStart = i
    else:
        series = 0

    i += 1
    if (i % 100 == 0):
        print (i)

print (seriesStart)
