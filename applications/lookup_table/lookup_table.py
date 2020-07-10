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

#print(slowfun_too_slow(3,2))


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    argument = (x,y)
    if argument not in cache:
        cache[argument] = math.pow(x,y)
        cache[argument] = math.factorial(cache[argument])
        cache[argument] //= (x + y)
        cache[argument] %= 982451653
    return cache[argument]
    

# Do not modify below this line!
'''
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
'''

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')