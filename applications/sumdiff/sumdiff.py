"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)

store results like so -> cache[f(a) + f(b)] = (a, b)
have to check the other values -> 
    z = f(c) - f(d)
    if z in cache:
        print(f"a: {cache[z][0]}, b: {cache[z][1]}, c: {c}, d: {d}")

this problem was problematic for me, and I ended up with a
solution that was not very functional for large inputs
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
ab = {}
cd = {}


def sumdiff(data):
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    # if (a, b) not in ab:
                    #     ab[(a, b)] = f(a) + f(b)
                    # if (c, d) not in cd:
                    #     cd[(c, d)] = f(c) - f(d)
                    # if ab[(a, b)] == cd[(c, d)]:
                    # print(
                    #     f"f({a}) + f({b}) = f({c}) - f({d}) = {ab[(a, b)]}")
                    x = f(a) + f(b)
                    if x == f(c) - f(d):
                        print(
                            f"f({a}) + f({b}) = f({c}) - f({d}) = {x}")

# classmate solution, better but still not efficient
# combos = {}
# count = 0
# for x in q:
#     for y in q:
#         count += 1
#         combos[count] = (x, y)

# for add in combos:
#     for sub in combos:
#         if f(combos[add][0]) + f(combos[add][1]) == f(combos[sub][0]) - f(combos[sub][1]):
#             print(f"f({combos[add][0]}) + f({combos[add][1]}) = f({combos[sub][0]}) - f({combos[sub][1]})")



if __name__ == "__main__":
    sumdiff(q)
    # print(f(3) + f(66), f(74) - f(2))
    # print(f(3) + f(65), f(129) - f(58))
    # print(f(3) + f(65), f(190) - f(119))
    # print(f(3) + f(62), f(175) - f(107))
    # print(f(3) + f(63), f(70) - f(1))
