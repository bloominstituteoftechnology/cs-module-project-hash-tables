# Your code here
import sys
import math
import random

# sys.path.insert(1, 'E:\Lambda\cs-module-project-hash-tables')

# from hashtable.hashtable import HashTable

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

ht = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    if (x, y) in ht:
        return ht[(x, y)]
    else:
        res = slowfun_too_slow(x, y)
        ht[(x,y)] = res
    return res
    



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
