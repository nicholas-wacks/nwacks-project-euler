sum = 0

def isPalindrome(s):
    return str(s) == str(s)[::-1]

for i in range(1, 1000000, 2):
    if (isPalindrome(i) and isPalindrome(bin(i)[2:])):
        sum += i

print(sum)
