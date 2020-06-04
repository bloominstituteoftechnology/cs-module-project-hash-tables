# 0 1 1 2 3 5 8 13 21 ...

def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

# for i in range(100):
#     print(f'{i:3} {fib(i)}') 

"""
# Start making the same calls over and over.
# fib(30) = fib(29) + fib(28)
# fib(29) = fib(28) + fib(27)
# fib(28) = fib(27) + fib(26)
# fib(28) = fib(27) + fib(26)
# fib(27) = fib(26) + fib(25)
# fib(27) = fib(26) + fib(25)
# fib(27) = fib(26) + fib(25)
# fib(26) = fib(25) + fib(24)
"""
######################################################
######################################################
######################################################

# Starts going REALLY slow. basically stalls out around 37. The time complextity is O(2^n)
# We should save some of this so that we aren't making the same calls over and over and over.
### LETS USE A HASH TABLE


# memoization => went super fast
cache = {}

def fib1(n):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fib1(n-1) + fib1(n-2)
    
    return cache[n]

# for i in range(100):
#     print(f'{i:3} {fib1(i)}') 

######################################################
######################################################
######################################################
# Inverse square root

# inv_sqrt(x) = 1 / sqrt(x)
import math 

inv_sqrt = {}

def build_lookup_table():

    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)

build_lookup_table()

# print(inv_sqrt[3])
# print(inv_sqrt[999])

######################################################
######################################################
######################################################

# Let's sort a dictionary/hash table

d = {
    'foo': 12, 
    'bar': 17,
    'qux': 2
}

items = list(d.items())

# Sort ascending by key
items.sort()

print(items)

# Sort descending by key
items.sort(reverse=True)

print(items)

# .sort sorts by key, but what about by value?
# TWo ways:
"""
(1)
def get_key(e): # e is going to be the tuple
    # Return the thing that we want to sort by
    return e[1] # value

items.sort(key=get_key)
"""
# (2)
items.sort(key=lambda e: e[1])
print(items)