
# Resizing an array is linear
# Pre-allocating is one option
my_arr = [None] * 100000000

# Pre-populate your cache
import math

def inverse_root(num):
    return 1 / math.sqrt(num)

    
cache = {}   

def populate_cache():
    for i in range(1, 1000):
        cache[i] = inverse_root(i)

populate_cache()

print(inverse_root(999))
print(cache[999])



# Lazy computation
# Lazily computed




    
# Hash table:
## Hash function
## Backed by an array
## Some way to handle collisions: Linked list (or use open addressing)

# Dictionaries and objects are just hash tables with a few methods added
## you could add a .items(), .values()