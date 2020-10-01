# Your code here
import math
import random
from hashtable import HashTable
import time

start = time.time()

power = HashTable(12*3)
factorial = HashTable(12*3)
division = HashTable(12*3)
modulo = HashTable(12*3)

# power = {}
# factorial = {}
# division = {}
# modulo = {}

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
        v = entry
    else:
        v = math.pow(x, y)
        power.put(p_key, v)
        #power[p_key] = v

    f_key = f'({p_key})!'
    entry = factorial.get(f_key)

    if entry:
        v = entry
    else:
        v = math.factorial(v)
        factorial.put(f_key, v)
        #factorial[f_key] = v

    denom = x + y
    d_key = f'{f_key}//({x} + {y})'
    entry = division.get(d_key)

    if entry:
        v = entry
    else:
        v //= denom
        division.put(d_key, v)
        #division[d_key] = v

    m_key = f'({d_key}) % 982451653'
    entry = modulo.get(m_key)

    if entry:
        return entry
    else:
        v %= 982451653
        modulo.put(m_key, v)
        #modulo[m_key] = v
        return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end = time.time()

print('Runtime: ', end - start)

#2.0707 with python dicts
#2.5381 with my hash table.  Not shabby