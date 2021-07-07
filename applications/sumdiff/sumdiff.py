"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
import itertools
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")
