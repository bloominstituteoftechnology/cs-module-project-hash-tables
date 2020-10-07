# Your code here
import math
from math import factorial
import random

math_hash = {}

for i in range(2, 14):
    for j in range(3, 6):
        power = math.pow(i, j)
        factorial = math.factorial(power)
        floor_division = factorial // (i + j)
        remainder = floor_division % 982451653
        
        math_hash[(i, j)] = remainder

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
    # Your code here
    return math_hash[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
