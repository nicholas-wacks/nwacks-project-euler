tri = []
squ = []
pen = []
hex = []
hep = []
oct = []

i = 1
m = 0
while (m < 10000):
    temp =  int((i * (i + 1)) / 2)
    m = temp
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        tri.append(temp)

    temp =  int(i * i)
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        squ.append(temp)

    temp =  int((i * ((3 * i) - 1)) / 2)
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        pen.append(temp)

    temp =  int(i * ((2 * i) - 1))
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        hex.append(temp)

    temp = int((i * ((5 * i) - 3)) / 2)
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        hep.append(temp)

    temp =  int(i * ((3 * i) - 2))
    if (temp > 999 and temp < 10000 and temp % 100 > 9):
        oct.append(temp)

    i += 1

def getCyclicSum(n, s, rSum, stream):
    if (len(s) == 0):
        initial = int(stream[:4])
        if (int(initial / 100) == n % 100):
            print (stream + ' ' + str(rSum))
            return rSum
        return 0

    for nums in s:
        tempSet = s[:]
        tempSet.remove(nums)
        for i in nums:
            if (n % 100 == int(i / 100) and str(i) not in stream):
                cs = getCyclicSum(i, tempSet, i + rSum, stream + ' ' + str(i) + "(" + names[len(nums)] + ")")
                if (cs != 0):
                    return cs
    return 0

names = { len(tri): 'tri', len(squ): 'squ', len(pen): 'pen', len(hex): 'hex', len(hep): 'hep', len(oct): 'oct' } 

sets = [tri[:], squ[:], pen[:], hex[:], hep[:]]

for o in oct:
    vs = getCyclicSum(o, sets, o, str(o) + "(" + names[len(oct)] + ")")
    if (vs != 0):
        print(vs)