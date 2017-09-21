def isPalindrome(n):
    return str(n) == str(n)[::-1]

count = 9999
for i in range(1, 10000):
    t = i
    steps = 0
    while(steps < 50):
        steps += 1
        t += int(str(t)[::-1])
        if (isPalindrome(t)):
            count -= 1
            break

print (count)