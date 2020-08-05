import random
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
#q = set(range(1, 200))
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
        potential_lefts[(a, b)] = (f(a) + f(b))

potential_rights = {}
for c in q:
    for d in q:
        potential_rights[(c, d)] = (f(c) - f(d))

for l_key, l_value in potential_lefts.items():
    for r_key, r_value in potential_rights.items():
        if l_value == r_value:
            matches.append((l_key, r_key))

print(matches)