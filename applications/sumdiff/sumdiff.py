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

# lol this isnt a hash table problem i cant even think of how to use one to solve it
# this is an itertools problem.
# or just like. combinations, permutations, and list building.
# and that is best case.