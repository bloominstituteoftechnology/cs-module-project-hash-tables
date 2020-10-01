# Imports
import random
import math

# Define a lookup table (dict)
lookup_dict = {}

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
    tmp_key = str(x) + "_" + str(y)

    # Does the lookup key exist in lookup_dict?
    if tmp_key in lookup_dict:
        # Found key, return precalculated value
        return lookup_dict[tmp_key]

    # Generate 
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    
    lookup_dict[tmp_key] = v

    return v

# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
