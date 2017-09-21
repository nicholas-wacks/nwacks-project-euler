from itertools import *

squares = ["01", "04", "06", "16", "25", "36", "46", "64", "81"]

def isValidCombo(s1, s2):
    d1 = set(s1[:])
    d2 = set(s2[:])
    if ("9" in d1):
        d1.add("6")
    if ("9" in d2):
        d2.add("6")
    for square in squares:
        if ((square[0] not in d1 or square[1] not in d2) and (square[0] not in d2 or square[1] not in d1)):
            return False
    return True

count = 0

for d1 in combinations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 6):
    for d2 in combinations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 6):
        if (isValidCombo(d1, d2)):
            count += 1
            print (str(d1) + " - " + str(d2))

print(count / 2)