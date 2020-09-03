"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def combo(lst, n):

    if n == 0:
        return [[]]

    l1 = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]

        for p in combo(remLst, n-1):
            l1.append([m] + p)

    return l1


def same(r, lst):
    for i in range(0, len(lst)):
        r.append([lst[i], lst[i]])
    return r


results = combo(q, 2)
results = same(results, q)
print(results)

add_dict = {}
for i in results:
    i = tuple(i)
    add_dict[i] = f(i[0]) + f(i[1])

for k, v in add_dict.items():
    print(k, v)

print(' ')

subtract_dict = {}
for i in results:
    i = tuple(i)
    subtract_dict[i] = f(i[1]) - f(i[0])

for k, v in subtract_dict.items():
    print(k, v)

for k1, v1 in add_dict.items():
    for k2, v2 in subtract_dict.items():
        if v1 == v2:
            # print(k1, k2, v1)
            print('f(', k1[0], ') + f(', k1[1], ') = f(', k2[1], ') - f(', k2[0], ')', v1)
