# Your code here
import math
import random
from hashtable import HashTable


factorial = HashTable()
power = HashTable()
division = HashTable()
modulo = HashTable()

def part_fact(start, value, end):
    for i in range(start + 1, end):
        value *= i
    return value

def nearest_fact(value):
    # because the test case won't generate less than 8 factorial
    # a little specific an hacky, but fine for this example since we don't have
    # unit tests to consider.
    for i in range(int(value), 7, -1):
        entry = factorial.get(str(i))
        if entry:
            return (i, entry)
    return (None, None)



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
    global factorial, power, division, modulo


    p_key = f'{x}^{y}'
    entry = power.get(p_key)

    if entry:
        print('found power')
        v = entry
    else:
        v = math.pow(x, y)
        power.put(p_key, v)

    f_key = f'{v}'
    entry = factorial.get(f_key)

    # TODO: Consider looking for the nearest factorial and computing from there

    if entry:
        print('found factorial')
        v = entry
    else:
        i, nearest = nearest_fact(v)
        if i:
            v = part_fact(1, nearest, v)
            factorial.put(f_key, v)
        else:
            v = math.factorial(v)
            factorial.put(f_key, v)

    denom = x + y
    d_key = f'{v}//{denom}'
    entry = division.get(d_key)

    # TODO: Consider common denoms

    if entry:
        print('found division')
        v = entry
    else:
        v //= denom
        division.put(d_key, v)

    m_key = f'{v}'
    entry = modulo.get(m_key)

    if entry:
        print('found modulo')
        return entry
    else:
        v %= 982451653
        modulo.put(m_key, v)
        return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
