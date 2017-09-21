def getLargestPalindromeProduct(max):
    highest = 0
    for i in range(max + 1):
        for j in range(i + 1):
            product = (max - i) * (max - j)
            if (isPalindrome(product) and product > highest):
                highest = product
    return highest

def isPalindrome(n):
    return str(n) == str(n)[::-1]

print (getLargestPalindromeProduct(99))
print (getLargestPalindromeProduct(999))