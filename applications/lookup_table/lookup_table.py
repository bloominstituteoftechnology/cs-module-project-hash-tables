# Your code here
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# imagine this is in a class so I can store a lookup table
# and not lose my data every time I run the function
lookup_table = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if str(f'{x}, {y}') not in lookup_table:
        lookup_table[str(f'{x}, {y}')] = slowfun_too_slow(x, y)
        return lookup_table[str(f'{x}, {y}')]
    else:
        return lookup_table[str(f'{x}, {y}')]

import random
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
