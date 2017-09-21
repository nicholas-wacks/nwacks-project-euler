baseDig = 10
done = False

while (not done):
    i = baseDig
    while (i * 6 < baseDig * 10):
        good = True
        for j in range(2, 7):
            if (sorted(str(i)) != sorted(str(i * j))):
                good = False
                break
        if (good):
            print(i)
            done = True
        i += 1
    baseDig *= 10
    print(baseDig)