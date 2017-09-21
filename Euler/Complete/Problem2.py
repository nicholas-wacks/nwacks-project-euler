def sumOfEvenFibonacci(n):
    a = 0
    b = 1
    sum = 0
    while (b <= n):
        if (b % 2 == 0):
            sum += b
        c = a + b
        a = b
        b = c
    return sum

print (sumOfEvenFibonacci(4000000))