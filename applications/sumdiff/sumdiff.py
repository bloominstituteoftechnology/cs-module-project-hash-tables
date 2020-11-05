"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

add_results = {}
sub_results = {}

def f(x):
    return x * 4 + 6

def solve(q):
    results = []

    for i in range(len(q)):
        for j in range(len(q)):
            add_results[(q[i], q[j])] = f(q[i]) + f(q[j])
            sub_results[(q[i], q[j])] = f(q[i]) - f(q[j])

    for a in add_results:
        for s in sub_results:
            if add_results[a] == sub_results[s]:
                result = f"{f(a[0])} + {f(a[1])} = {f(s[0])} - {f(s[1])}"
                results.append(result)

    return results


print(solve(q))
