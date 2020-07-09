"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
#q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


additions = {}
subtractions = {}

for n1 in q:
    for n2 in q:
        add = f(n1) + f(n2)
        sub = f(n1) - f(n2)
        if add in additions.keys():
            additions[add].append((n1, n2))
        else:
            additions[add] = [(n1, n2)]
        if sub in subtractions.keys():
            subtractions[sub].append((n1, n2))
        else:
            subtractions[sub] = [(n1, n2)]
results = []
for a_total in additions.keys():
    if a_total in subtractions.keys():
        for a_comb in additions[a_total]:
            for b_comb in subtractions[a_total]:
                # print(f"{a_comb}: {b_comb}")
                results.append(f"{a_comb}: {b_comb}")
print(len(results))
