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
cache = {}
sums = {}

for sm in sums:
    if sm in diff:
        for l in sums[sm]:
            for k in diff[u]:
                if l == k:
                    a,b = l[0],l[1]
                    c,d = k[0], k[1]

