import random
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

matches = []

# nest for loops for every combination of a and b, 
# them pick c and d to match?
potential_lefts = {}
for a in q:
    for b in q:
        potential_lefts[(f(a) + f(b))] = (a, b) # key is sum, value is index

potential_rights = {}
for c in q:
    for d in q:
        potential_rights[(f(c) - f(d))] = (c, d)# key is diff, val is index

for ab in potential_lefts:
    if ab in potential_rights:
        left_indexes = potential_lefts[ab]
        right_indexes = potential_rights[ab]
        matches.append(left_indexes)
        matches.append(right_indexes)

print(matches)
# lesson learned: the thing you want to search quickly should be set to the keys