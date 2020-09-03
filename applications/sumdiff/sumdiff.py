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

def printCombs(q):
    cache = {}
    sums = []
    diff = []
    for i in q:
        for x in q:
            if i not in cache:
                fi = f(i)
                cache[i] = fi
            else:
                fi = cache[i]
            
            if x not in cache:
                fx = f(x)
                cache[x] = fx
            else:
                fx = cache[x]
            sums.append((fi,fx,fi+fx))
            diff.append((fi,fx,fi-fx))
    for i in sums:
        for x in diff:
            if i[-1] == x[-1]:
                print(f'f{i[0]} + f{i[1]} = f{x[0]} - f{x[0]} = {i[-1]}')

printCombs(q)