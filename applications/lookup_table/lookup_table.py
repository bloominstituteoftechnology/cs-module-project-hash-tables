import random
import math

def slowfun_too_slow(x, y): #1, 2
    v = math.pow(x, y) # 1 ^2 = 1
    v = math.factorial(v) # probably 1
    v //= (x + y)
    v %= 982451653

    return v

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    if x <= 1 or y <= 1:
        return x, y

    if (x, y) not in cache:
        v = math.pow(x, y) # 1 ^2 = 1
        v = math.factorial(v) # probably 1
        v //= (x + y)
        v %= 982451653

        cache[(x, y)] = v

    return cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
