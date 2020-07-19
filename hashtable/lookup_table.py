import math

lookup_table = {}

def inverse_root(n):
    return 1 / math.sqrt(n)

def populate_lookup_table(n):
    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)
    
populate_lookup_table()

#precomputing or lazy computing