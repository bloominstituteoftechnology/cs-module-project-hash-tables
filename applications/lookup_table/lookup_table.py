# Your code here

import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    return v


def slowfun(x, y, cache=dict()):
    if (x, y) not in cache:
        cache[(x, y)] = slowfun_too_slow(x, y)
    return cache[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
