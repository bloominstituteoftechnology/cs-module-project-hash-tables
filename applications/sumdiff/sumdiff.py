"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)

store results like so -> cache[f(a) + f(b)] = (a, b)
have to check the other values -> 
    z = f(c) - f(d)
    if z in cache:
        print(f"a: {cache[z][0]}, b: {cache[z][1]}, c: {c}, d: {d}")
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def sumdiff(data):
    for a in data:
        for b in data:
            for c in data:
                for d in data:
                    if f(a) + f(b) == f(c) - f(d):
                        print(f"a: {a}, b: {b}, c: {c}, d: {d}")


if __name__ == "__main__":
    sumdiff(q)
