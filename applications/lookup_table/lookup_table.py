# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    # 4^2 = 16
    v = math.factorial(v)
    # 16! = 20,922,789,888,000
    v //= (x + y)
    # v = 20,922,789,888,000 // 4+2
    # v = 10,461,394,944,000

    v %= 982451653
    # 10,461,394,944,000 %= 982451653

    return v

# def facto(num):
#     cache = {}
#     if num <= 1:
#         return 1
#     else:
#         if num not in cache:
#             result = num * facto(num - 1)
#             cache[num] = result
#         return cache[num]

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    if x == 0:
        return 0
    if y == 0:
        return 1

    cache = {}
    v = slowfun(x, y)
    
    if (x, y) not in cache:
        v = math.pow(x, y)
        cache[(x, y)] = v
    if (x, y) not in cache:
        v = math.factorial(v)
        cache[(x, y)] = v
    if (x, y) not in cache:
        v //= (x + y)
        cache[(x, y)] = v
    if (x, y) not in cache:
        v %= 982451653
        cache[(x, y)] = v
    return cache[(x, y)]



    # if x == 0:
    #     return 0
    # if y == 0:
    #     return 1

    # pow_cache = {}
    # fac_cache = {}
    # floor_cache = {}
    # modulo_cache = {}

    # v = 0

    # if (x, y) not in pow_cache:
    #     v = math.pow(x, y)
    #     if v not in fac_cache:
    #         v = math.factorial(v)
    #         if v not in floor_cache:
    #             v //= (x + y)
    #             if v not in modulo_cache:
    #                 v %= 982451653
    # return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
