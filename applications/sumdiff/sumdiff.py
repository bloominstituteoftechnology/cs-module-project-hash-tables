"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6
ht = {}
def sumdiff(arr, comb, fn):
    # print(arr)
    if tuple(comb[:4]) in ht:
        return
    if len(comb) >= len(arr):
        if fn(comb[0]) + fn(comb[1]) == fn(comb[2]) - fn(comb[3]):
            print(comb[:4])
            ht[tuple(comb[:4])] = True
        return
    for i,n in enumerate(arr):
        comb.append(n)
        sumdiff(arr, comb, fn)
        comb.pop()
sumdiff(q, [], f)
# Your code here

