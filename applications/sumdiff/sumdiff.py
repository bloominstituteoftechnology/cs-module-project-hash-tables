"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = (1, 3, 4, 7, 12)        # 2nd pass solution is faster by:  ~74.2%
#q = set(range(1, 10))      # 2nd pass solution is faster by:  ~96.1%
#q = set(range(1, 200))     # 2nd pass solution is faster by:  ~99.5%


def f(x):
    return x * 4 + 6

# Your code here
# a + b + 3 = c - d
# a = c - d - b - 3
# b = c - d - a - 3
# c = a + b + d + 3
# d = c - a - b - 3

# First pass solution
def equivalentSumsAndDiffs(q):
    solutionSet = set()
    for a in q:
        for b in q:
            for c in q:
                for d in q:
                    if a == c - d - b - 3:
                        solutionSet.add((a, b, c, d))
    return list(solutionSet)

def printEquivalentSumsAndDiffs(q):
    results = equivalentSumsAndDiffs(q)
    for r in results:
        print(f"f({r[0]}) + f({r[1]}) = f({r[2]}) - f({r[3]})    {f(r[0])} + {f(r[1])} = {f(r[2])} - {f(r[3])}")



# Second pass solution
def equivalentSumsAndDiffs2(q):
    l = list(q)
    minQ = min(q)
    maxQ = max(q)
    n = len(q)
    solutionSet = set()
    for a in range(0, n):
        if l[a] + 2*minQ + 3 > maxQ:
            break
        for b in range(a, n):
            if l[a] + l[b] + minQ + 3 > maxQ:
                break
            for d in range(b, n):
                if l[a] + l[b] + l[d] + 3 > maxQ:
                    break
                elif l[a] + l[b] + l[d] + 3 in q:
                    c = l[a] + l[b] + l[d] + 3
                    solutionSet.add((l[a], l[b], c, l[d]))
                    solutionSet.add((l[a], l[d], c, l[b]))
                    solutionSet.add((l[b], l[a], c, l[d]))
                    solutionSet.add((l[b], l[d], c, l[a]))
                    solutionSet.add((l[d], l[a], c, l[b]))
                    solutionSet.add((l[d], l[b], c, l[a]))
    return list(solutionSet)

def printEquivalentSumsAndDiffs2(q):
    results = equivalentSumsAndDiffs2(q)
    for r in results:
        print(f"f({r[0]}) + f({r[1]}) = f({r[2]}) - f({r[3]})    {f(r[0])} + {f(r[1])} = {f(r[2])} - {f(r[3])}")


printEquivalentSumsAndDiffs2(q)


import time

# Time how long it takes the first pass solution to run
start = time.process_time()
equivalentSumsAndDiffs(q)
firstPassDuration = time.process_time() - start

# Time how long it takes the second pass solution to run
start = time.process_time()
equivalentSumsAndDiffs2(q)
secondPassDuration = time.process_time() - start

print("\nThe first pass solution took %.6f seconds." % firstPassDuration)
print("The second pass solution took %.6f seconds." % secondPassDuration)

percentFaster = (firstPassDuration - secondPassDuration) * 100 / firstPassDuration
print("\nThe second pass solution is %.1f%% faster" % percentFaster)