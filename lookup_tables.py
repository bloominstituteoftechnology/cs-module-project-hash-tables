
import math

lookup_table = {}

def inverse_root(n):
    return 1 / math.sqrt(n)

def populate_lookup_table():

    for i in range(1, 1000):
        lookup_table[i] = inverse_root(i)

populate_lookup_table()

print(lookup_table[25])
print(lookup_table[932])

# precomputing

# lazily computing