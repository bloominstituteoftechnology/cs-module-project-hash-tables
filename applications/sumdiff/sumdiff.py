"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import itertools
import math
#q = set(range(1, 10))
q = set(range(1, 200))
#q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

def sumDiff(q):
    possibles = list(itertools.combinations(q,2))
    possiblesums = []
    possiblesubtractions = []
    for i in possibles:
        possiblesums.append(f(i[0]) + f(i[1]))
        possiblesubtractions.append(f(i[1]) - f(i[0]))

    for i in range(len(possiblesums) -1):
        for j in range(len(possiblesubtractions) -1):
            if possiblesums[i] == possiblesubtractions[j]:
                print(f'f({possibles[i][0]}) + f({possibles[i][1]}) == f({possibles[j][1]}) - f({possibles[j][0]})       {f(possibles[i][0])} + {f(possibles[i][1])} = {f(possibles[j][1])} - {f(possibles[j][0])}')
                print(f'f({possibles[i][1]}) + f({possibles[i][0]}) == f({possibles[j][1]}) - f({possibles[j][0]})       {f(possibles[i][1])} + {f(possibles[i][0])} = {f(possibles[j][1])} - {f(possibles[j][0])}')
sumDiff(q)
