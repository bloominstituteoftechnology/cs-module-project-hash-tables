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

sums = {}
diffs = {}

def build_sum_lookup(q):

    for a in range(len(q)):
        for b in range(len(q)):
            sum = f(q[a]) + f(q[b])
            sums[(q[a], q[b])] = sum

def build_diff_lookup(q):

    for c in range(len(q)):
        for d in range(len(q)):
            if q[c] >= q[d]:
                diff = f(q[c]) - f(q[d])
                diffs[(q[c], q[d])] = diff

build_sum_lookup(q)
build_diff_lookup(q)

def sumdiff(q):

    for a in range(len(q)):
        for b in range(len(q)):
            for c in range(len(q)):
                for d in range(len(q)):
                    if q[c] >= q[d]:
                        if sums[(q[a], q[b])] == diffs[(q[c], q[d])]:
                            print((q[a], q[b]), (q[c], q[d]))

sumdiff(q)