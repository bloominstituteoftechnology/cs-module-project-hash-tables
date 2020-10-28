# Your code here
import math
import random

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    if x == 0:
        return 0
    
    if y == 0:
        return 1

    index = (x, y)

    if index not in cache:
        cache[index] = slowfun_too_slow(x, y)

    return cache[index]

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
