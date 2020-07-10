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

# create reverse lookup table
# keys: the result
# values: list of tuples of numbers that make that result
lookup_add = {}
lookup_sub = {}
for i in q:
    for j in q:
        add = f(i) + f(j)
        sub = f(i) - f(j)
        if add not in lookup_add:
            lookup_add[add] = [(i, j)]
        else:
            lookup_add[add].append((i, j))
        if sub not in lookup_sub:
            lookup_sub[sub] = [(i, j)]
        else:
            lookup_sub[sub].append((i, j))

# get all matches
matches = []
for a_plus_b in lookup_add:
    if a_plus_b in lookup_sub:
        # get matching values
        matched_adds = lookup_add[a_plus_b]
        matched_subs = lookup_sub[a_plus_b]
        # print(matched_adds)
        # go through each tuple of numbers
        for a_b in matched_adds:
            for c_d in matched_subs:
                matches.append((a_b[0], a_b[1], c_d[0], c_d[1]))

for m in matches:
    print(f'f({m[0]}) + f({m[1]}) = f({m[2]}) - f({m[3]})',
          f'\t{f(m[0])} + {f(m[1])} = {f(m[2])} - {f(m[3])}')
