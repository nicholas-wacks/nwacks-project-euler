import math

values = dict()
values[0] = 0
values[1] = 3
values[2] = 3
values[3] = 5
values[4] = 4
values[5] = 4
values[6] = 3
values[7] = 5
values[8] = 5
values[9] = 4
values[10] = 3
values[11] = 6
values[12] = 6
values[13] = 8
values[14] = 8
values[15] = 7
values[16] = 7
values[17] = 9
values[18] = 8
values[19] = 8
values[20] = 6
values[30] = 6
values[40] = 5
values[50] = 5
values[60] = 5
values[70] = 7
values[80] = 6
values[90] = 6

sum = 11

for i in range(1, 1000):
    v = i
    if (v >= 100):
        sum += values[math.floor(v / 100)] + 7
        if (i % 100 == 0):
            continue
        v = i % 100
        sum += 3

    if (v <= 20):
        sum += values[v]
    else:
        sum += values[v % 10] + values[v - (v % 10)]


print(sum)