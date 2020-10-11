from collections import defaultdict


"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here


f_of = {}
for x in q:
    f_of[x] = f(x)

sums = defaultdict(list)
for i in q:
    for j in q:
        f_of_i = f_of[i]
        f_of_j = f_of[j]
        sums[f_of_i + f_of_j].append((f"f({i}) + f({j})", f"{f_of_i} + {f_of_j}"))

for i in q:
    for j in q:
        f_of_i = f_of[i]
        f_of_j = f_of[j]
        difference = f_of_i - f_of_j
        if difference in sums:
            for sum in sums[difference]:
                print(
                    f"{sum[0]} = f({i}) - f({j})   {sum[1]} = " f"{f_of_i} - {f_of_j}"
                )
