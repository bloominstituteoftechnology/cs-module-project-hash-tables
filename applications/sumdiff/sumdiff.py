"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
# a = c - d - b - 3
# b = c - d - a - 3
# c = a + b + d + 3
# d = c - a - b - 3

def equivalentSumsAndDiffs(q):
    results = []
    for a in q:
        for b in q:
            for c in q:
                for d in q:
                    if a == c - d - b - 3:
                        results.append([a, b, c, d])
    return results

def printEquivalentSumsAndDiffs(q):
    results = equivalentSumsAndDiffs(q)
    for r in results:
        print(f"f({r[0]}) + f({r[1]}) = f({r[2]}) - f({r[3]})    {f(r[0])} + {f(r[1])} = {f(r[2])} - {f(r[3])}")
    
printEquivalentSumsAndDiffs(q)
