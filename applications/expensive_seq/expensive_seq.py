# Your code here
import math
import random

# cache = {}

def expensive_seq(x, y, z, cache=None):
    # Your code here
    if cache is None:
        cache = {}
    if (x, y, z) in cache:
        return cache[(x,y,z)]
    elif x <= 0:
        cache[(x,y,z)] = y + z
        return y + z
    else:
        result = (
            expensive_seq(x - 1, y + 1, z, cache) + expensive_seq(x - 2, y + 2, z * 2, cache) + expensive_seq(x - 3, y + 3, z * 3, cache)
        )

    cache[(x,y,z)] = result
    return cache[(x,y,z)]

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
