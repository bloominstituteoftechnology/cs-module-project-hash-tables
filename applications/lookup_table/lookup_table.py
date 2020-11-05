import math
import random 

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v

def slowfun(x, y):
    if (x, y) in lookup_table:
        return lookup_table[(x, y)]
    elif (x,y) not in lookup_table:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        lookup_table[(x, y)] = v 
        return v
    
lookup_table = {}

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    lookup_table[(x,y)] = slowfun(x, y)

    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

