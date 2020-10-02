import math
import random

my_lookup = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    v = math.pow(x, y)
    if v in my_lookup:
        v = my_lookup[v]
    else:
        my_lookup[v] = math.factorial(v)
        v = my_lookup[v]
    v //= (x + y)
    v %= 982451653
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
