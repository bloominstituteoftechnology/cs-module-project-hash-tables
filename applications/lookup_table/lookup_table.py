# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def build_lookup_table():
    d = {}

    for x in range(2, 14):
        for y in range(3, 6):
            d[(x, y)] = slowfun_too_slow(x, y)

    return d

# this ensures that the lookup table is ALREADY BUILT before we call slowfun() in our for loop!
table = build_lookup_table()

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    return table[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')