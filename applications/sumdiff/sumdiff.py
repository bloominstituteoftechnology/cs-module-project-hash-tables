"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

cache = dict()


def f(x):
    return x * 4 + 6


print(cache)
plus_cache = dict()
minus_cache = dict()

results = []


def find_pairs():
    for val in q:
        for i in range(len(q)):
            if (val, q[i]) not in plus_cache:
                plus_cache[(val, q[i])] = f(val) + f(q[i])
            if ((val, q[i])) not in minus_cache:
                minus_cache[(q[i], val)] = f(q[i]) - f(val)

    for p in plus_cache.items():
        for m in minus_cache.items():
            if p[1] == m[1]:
                results.append(f'{p[0]} = {m[0]}')
    print(results)


find_pairs()
print(plus_cache, '+++')
print(minus_cache, '-----')
# def findCombinations():
#     c = dict()
#     q = list(cache.q())
#     if a + b == c - d:
#     def helper(n=0, seen=[]):
#         if n == len(q):
#             results.append(seen)
#             return
#         for i in range(len(q)):
#             helper(n=n + 1, seen=seen + [q[i]])
#     helper()
#     print(results)

# findCombinations()


# Your code here
