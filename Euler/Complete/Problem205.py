#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

peterProbabilities = {}
colinProbabilities = {}

for c1 in range(1, 7):
    for c2 in range(1, 7):
        for c3 in range(1, 7):
            for c4 in range(1, 7):
                for c5 in range(1, 7):
                    for c6 in range(1, 7):
                        roll = c1 + c2 + c3 + c4 + c5 + c6
                        if (roll in colinProbabilities):
                            colinProbabilities[roll] += 1
                        else:
                            colinProbabilities[roll] = 1

cTotalRolls = sum(colinProbabilities.values())
for c in colinProbabilities.keys():
    colinProbabilities[c] /= cTotalRolls

for p1 in range(1, 5):
    for p2 in range(1, 5):
        for p3 in range(1, 5):
            for p4 in range(1, 5):
                for p5 in range(1, 5):
                    for p6 in range(1, 5):
                        for p7 in range(1, 5):
                            for p8 in range(1, 5):
                                for p9 in range(1, 5):
                                    roll = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                                    if (roll in peterProbabilities):
                                        peterProbabilities[roll] += 1
                                    else:
                                        peterProbabilities[roll] = 1

pTotalRolls = sum(peterProbabilities.values())
for p in peterProbabilities.keys():
    peterProbabilities[p] /= pTotalRolls

peteWinRate = 0

for p in peterProbabilities.keys():
    for c in colinProbabilities.keys():
        if (p > c):
            peteWinRate += peterProbabilities[p] * colinProbabilities[c]

print (peteWinRate)
