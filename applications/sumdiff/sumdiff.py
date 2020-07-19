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
#set addition and subtraction dicts
addition = {}
subtraction = {}

for i in range(0, len(q)):
    for j in range(0, len(q)):
        addition[f'f({q[i]}) + f({q[j]})'] = f(q[i]) + f(q[j])
        subtraction[f'f({q[j]}) - f({q[i]})'] = f(q[j]) + f(q[i])

for add in addition:
    for sub in subtraction:
        if subtraction[sub] == addition[add]:
            print(f'{add} = {sub} = {addition[add]}')
