# Your code here
import math
import random

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v) # worse time ever
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # we want to compute the power value 
    new_v = math.pow(x, y)
    if new_v not in cache:
        cache[new_v] = math.factorial(new_v)
        new_v = cache[new_v]
    else:
        new_v = cache[new_v]
    
    new_v //= (x + y)
    new_v %= 982451653
    
    return new_v
    
    # we want to execute the factorial

    # and store that value in our cache
    # execute floor division
    # execute module operation 
    # return that cache value
    


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
