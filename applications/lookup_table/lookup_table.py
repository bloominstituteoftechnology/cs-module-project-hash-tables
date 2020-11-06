# Your code here
import random
import math

cache = {}


def slowfun_too_slow(x, y):
    if (x, y) in cache:
        return (x, y)
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[(x, y)] = v
    return v


def slowfun(x, y):
    pass
    # Your code here


    # Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
