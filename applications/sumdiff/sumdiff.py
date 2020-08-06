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
# Duplicate q values allowed
# This means 5^4 or 625 possible combinations to test if equal
# Obviously some will be duplicates because of additions transative property.
# Tuples are immutable but indexable

# If found

# Iterator
for index1, item1 in enumerate(q):
    for index2, item2 in enumerate(q):
        for index3, item3 in enumerate(q):
            for index4, item4 in enumerate(q):
                if ((f(item1) + f(item2)) == (f(item3) - f(item4))):
                    print(f'f({item1}) + f({item2}) = f({item3}) - f({item4})    {f(item1)} + {f(item1)} = {f(item1)} - {f(item1)}')
