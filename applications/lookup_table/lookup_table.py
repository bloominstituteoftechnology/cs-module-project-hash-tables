# Your code here
import math
import random
import time

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y, cache={}):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = math.pow(x, y)
    if int(v) in cache:
        v = cache[v]
    else:
        x = int(v)
        v = math.factorial(int(v))
        cache[x] = v
    v //= (x + y)
    v %= 982451653
    return v

# Do not modify below this line!
start_time = time.time()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time = time.time()
print(f"50k times took {end_time - start_time} seconds")