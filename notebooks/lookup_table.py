"""
Import Statements
"""

import math

# Inverse


inv_sqrt = {}

# taking data to construct


def build_lookup_table():

    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)


build_lookup_table()

print(inv_sqrt[3])
print(inv_sqrt[12])
