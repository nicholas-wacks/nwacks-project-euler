max = 0

print("".join(sorted("4231")))

for i in range(9, 10000):
    val = ""
    j = 1
    while (len(val) < 9):
        val += str(i * j)
        j += 1

    if ("".join(sorted(val)) == "123456789" and int(val) > max):
        max = int(val)

print (max)