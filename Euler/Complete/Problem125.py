def isPalindrome(n):
    return str(n) == str(n)[::-1]

first = 1
top = 10 ** 8
count = 0
nums = set()

while ((first ** 2) + ((first + 1) ** 2) < top):
    temp = first ** 2
    j = first + 1

    while (temp < top):
        temp += j ** 2
        j += 1
        if (temp < top and isPalindrome(temp) and not temp in nums):
            count += 1
            nums.add(temp)

    first += 1
    if (first % 100 == 0):
        print(first)

print(count)
print(sum(nums))