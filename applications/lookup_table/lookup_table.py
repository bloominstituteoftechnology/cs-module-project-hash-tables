# Your code here
import math
import random
from hashtable import HashTable


factorial = HashTable()
power = HashTable()
division = HashTable()
modulo = HashTable()


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
    p_key = f'{x}^{y}'
    entry = power.get(p_key)

    if entry:
        v = entry
    else:
        v = math.pow(x, y)
        power.put(p_key, v)

    f_key = f'{v}'
    entry = factorial.get(f_key)

    # TODO: Consider looking for the nearest factorial and computing from there

    if entry:
        v = entry
    else:
        v = math.factorial(v)
        factorial.put(f_key, v)

    denom = x + y
    d_key = f'{v}//{denom}'
    entry = division.get(d_key)

    if entry:
        v = entry
    else:
        v //= denom
        division.put(d_key, v)

    m_key = f'{v}'
    entry = modulo.get(m_key)

    if entry:
        return entry
    else:
        return v % 982451653


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
