def getLargestPrimeFactor(n):
    i = 3

    while (n % 2 == 0 and n > 2):
        n /= 2

    while (i*i <= n):
        if (n % i == 0):
            n /= i
        else:
            i += 2
    return n

print (getLargestPrimeFactor(9))
print (getLargestPrimeFactor(32))
print (getLargestPrimeFactor(600851475143))