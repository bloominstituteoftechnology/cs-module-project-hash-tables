"""
Find all a, b, c, d in q such that f(a) + f(b) = f(c) - f(d).
"""
from collections import defaultdict

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    """
    Function as defined above.
    """
    return x * 4 + 6


f_of = {}
for x in q:
    f_of[x] = f(x)

# Create a dictionary whose keys are all possible sums f(a) + f(b), for some a
# and b in q and whose values are lists of all possible ways to reach each such
# sum.
sums = defaultdict(list)
for i in q:
    for j in q:
        f_of_i = f_of[i]
        f_of_j = f_of[j]
        sums[f_of_i + f_of_j].append((f'f({i}) + f({j})',
                                      f'{f_of_i} + {f_of_j}'))
# For each possible difference f(c) - f(d), for some c and d in q, check to see
# if that difference is in our previously generated list of sums. If it is,
# then print out the corresponding equations.
for i in q:
    for j in q:
        f_of_i = f_of[i]
        f_of_j = f_of[j]
        difference = f_of_i - f_of_j
        if difference in sums:
            for sum in sums[difference]:
                print(f'{sum[0]} = f({i}) - f({j})   {sum[1]} = '
                      f'{f_of_i} - {f_of_j}')
