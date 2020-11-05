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

import itertools

combinations = list(itertools.product(q, q))

for x in combinations:
    for y in combinations:
        if f(x[0]) + f(x[1]) == f(y[0]) - f(y[1]):
            print(f"f({x[0]}) + f({x[1]}) = f({y[0]}) - f({y[1]})" + "    " + str(f(x[0])) + " + " + str(f(x[1])) + " = " + str(f(y[0])) + " - " + str(f(y[1])))
