
cache = {}
import math

def inverse_root(x):
    return 1/math.sqrt(x)


def build_lookup_table():
    for i in range(1, 10000):
        cache[i] = inverse_root(i)
        
def get_inverse_root(x) :
    if x in cache:
        return cache[x] 
    else:
        cache[x]=inverse_root(x) 
        return cache[x]
print(get_inverse_root(9))    