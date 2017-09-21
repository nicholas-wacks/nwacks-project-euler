import math

def getSpecialTriplet(n):
    a = 1
    b = 1
    c = 1

    while (a + b + c != n):
        b = a
        while (a + b + c < n):
        
            while (a + b + c < n):
                if (math.sqrt(a**2 + b**2).is_integer()):
                    c = math.sqrt(a**2 + b**2)
                    if (a + b + c == n):
                        return (a * b * c)
                b += 1
            a+= 1
            b = a
    return 0

print (getSpecialTriplet(1000))