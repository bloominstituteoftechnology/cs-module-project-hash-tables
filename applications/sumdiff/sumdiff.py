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
diff = {}

for x in q:
    for y in q:
        add = f(x) + f(y)
        if add in sums:
            sums[add].append((x,y))
        else:
            sums[add] = [(x,y)]
        sub = f(x) - f(y)
        if sub in diff:
            diff[sub].append((x,y))
        else:
            diff[sub] = [(x,y)]


for key in sums:
    if key in diff:
        for value in sums[key]:
            for dvalue in diff[key]:
                A,B,C,D = value[0], value[1], dvalue[0], dvalue[1]
                assert(f(A) + f(B) == f(C), - f(D))
                print(f'f({A}) + f({B}) = f({C}) - f({D})'
                    f'    {f(A)} + {f(B)} = {f(C)} - {f(D)}')