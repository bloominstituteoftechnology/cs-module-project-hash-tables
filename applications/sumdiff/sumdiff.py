"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

import itertools

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

combos = list(itertools.product(q, q))

for x in combos:
    for y in combos:
        if f(x[0]) + f(x[1]) == f(y[0]) - f(y[1]):
            print(f"f({x[0]}) + f({x[1]}) = f({y[0]}) - f({y[1]})")
# Your code here

