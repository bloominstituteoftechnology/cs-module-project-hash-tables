import math

lookup_table = {}
# for n in range(1, 1001):
#     lookup_table[n] = 1 / math.sqrt(n)

# def inv_sqrt(n):
#     """n is an int between 1 and 1000"""

#     # return 1 / math.sqrt(n)
#     return lookup_table[n]

# print(inv_sqrt(10))
# print(inv_sqrt(100))

def lazy_inv_sqrt(n):
    """n is an int between 1 and 1000"""

    if n not in lookup_table:
        lookup_table[n] = 1 / math.sqrt(n)

    # return 1 / math.sqrt(n)
    return lookup_table[n]

print(lazy_inv_sqrt(10))
print(lazy_inv_sqrt(100))