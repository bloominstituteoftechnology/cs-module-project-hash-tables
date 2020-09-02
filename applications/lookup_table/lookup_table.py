import math
import random


number_set = {}

def slowfun_too_slow(x, y):
    # store value of x^y
    v = math.pow(x, y)
    # reassign v to the factorial value of v
    v = math.factorial(v)
    #  Divide the factorial by (x + y)
    v //= (x + y)
    # Get the mod of v for 982451653
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) not in number_set:
        result = math.pow(x, y)
        factorial = math.factorial(result)
        division = factorial // (x + y)
        mod = division % 982451653
        number_set[(x, y)] = (result, factorial, division, mod)
        number_set[(y, x)] = (result, factorial, division, mod)
    value = number_set[(x, y)]
    return value[3]
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
