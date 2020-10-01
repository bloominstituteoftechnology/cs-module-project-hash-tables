# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# cache = [[None] * 4] * 13 
# cache = []
# for i in range(13):
#     new_lst = []
#     for j in range(4):
#         new_lst.append(None)
#     cache.append(new_lst)


# def slowfun(x, y):
#     """
#     Rewrite slowfun_too_slow() in here so that the program produces the same
#     output, but completes quickly instead of taking ages to run.
#     """
#     # Your code here
#     # lst = [None] * 13
#     # lst2 = []
#     # for i in range(13):
#     #     lst2.append(None)
#     if x < 2 or x > 14 or y < 3 or y > 6: 
#         return None
#     if cache[x - 2][y - 3] is None:
#         cache[x - 2][y - 3] = slowfun_too_slow(x, y)

#     return cache[x - 2][y - 3]
    
cache = {}
def slowfun(x, y):
    if (x, y) in cache:
        return cache[(x, y)]
    if x < 2 or x > 14 or y < 3 or y > 6: 
        return None
    
    cache[(x, y)] = slowfun_too_slow(x, y)

    return cache[(x, y)]
    


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
