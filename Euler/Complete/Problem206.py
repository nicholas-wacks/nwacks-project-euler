#Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
#   where each “_” is a single digit.
import math, re

regexMatch = '1.2.3.4.5.6.7.8.9.0'

#Must end in a 0 to fit the pattern for the last 0
num = math.ceil(1929394959697989990 ** 0.5)
num = num - (num % 10) + 10

while (not re.match(regexMatch, str(num ** 2))):
    num -= 10
    if (re.match('.*3.4.5.6.7.8.9.0', str(num ** 2))):
        print (str(num) + ': ' + str(num **2))

print (str(num) + ': ' + str(num **2))