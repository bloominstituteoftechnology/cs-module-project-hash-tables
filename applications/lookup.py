# Lookup table


import math

# Build a lookup table for inverse square root for numbers 1 - 1000.

inv_sqrt_table = {}

def inv_sqrt(n):
	if n not in inv_sqrt_table:
		inv_sqrt_table[n] = 1 / math.sqrt(n)

	return inv_sqrt_table[n]

def build_lookup_table():
	for i in range(1, 10000001):
		inv_sqrt_table[i] = inv_sqrt(i)

build_lookup_table()

#print(inv_sqrt_table[10])
#print(inv_sqrt_table[37])


print(inv_sqrt(10))
print(inv_sqrt(37))
print(inv_sqrt(10000000000))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
