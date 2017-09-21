import math

index = 11
a = 55
b = 89

while (math.log10(b) < 999):
    c = a + b
    a = b
    b = c
    index += 1
    if (index % 100 == 0 or index > 4780):
        print(str(index) + ': ' + str(b))

print (b)
print (index)