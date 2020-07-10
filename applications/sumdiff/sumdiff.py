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
addcache = {}
subcache = {}
for i in range(0,len(q)):
    for j in range(0, len(q)):
        addcache[f'f({q[i]}) + f({q[j]})'] = f(q[i]) + f(q[j])
        subcache[f'f({q[j]}) - f({q[i]})'] = f(q[j]) - f(q[i])

for fromAdd in addcache:
    for fromSub in subcache:
        if subcache[fromSub] == addcache[fromAdd]:
            print(f'{fromAdd} = {fromSub} = {addcache[fromAdd]}')
#print(addcache)
#print(subcache)