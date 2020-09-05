# Your code here
import math
import random

powCache = {} # cache for the power
factCache = {} # cache for the factorial
divCache = {} # cache for the div
complete = {} # this is the cache for the whole function

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v) # factorial is 5 == 1 * 2 * 3 *4 *5
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) in complete: # once it has been done complete the value will be stored here
        return complete[(x,y)]
    # Your code here
    if (x,y) in powCache: # checking to see if it is in a cache, if it is will  use from there
        v = powCache[(x,y)]
    else:
        v = powCache[(x,y)] = math.pow(x,y) # if not in the cache, then will do the calculation and then use the val
    if v in factCache:
        v = factCache[v]
    else:
        v = factCache[v] = math.factorial(v)
    if (v, (x+y)) in divCache:
        v = divCache[(v,(x+y))]
    else:
        z = v//(x+y)
        v = divCache[(v,(x+y))] = z
    
    v %=982451653
    # if we get here will put in the complete the full value
    complete[(x,y)] = v
    return v





# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
