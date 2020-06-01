import random, math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

remainders = {}
unique_count = 0
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """    
    # products = {}
    # factorials = {}
    # quotients = {}
    
    def helper(a, b):
        x = math.pow(a, b)
        # build_products(a, b)
        y = math.factorial(x)
        # build_factorials(products[(a, b)])
        # print(products[(a, b)])
        z = y // (a + b)
        remainders[(a, b)] =  z % 982451653

    def build_products(a, b):
        total = 1
        for i in range(b + 1):
            products[a, i] = total
            total *= a

    def build_factorials(num):
        while num not in factorials:
            if num + 1 in factorials:
                factorials[num] = factorials[num + 1] / num + 1
                if num:
                    num -= 1
            elif num - 1 in factorials:
                factorials[num] = factorials[num - 1] * num
            else:
                factorials[num] = math.factorial(num)


    if (x, y) not in remainders:
        # for i in range(1, x+1):
            # for j in range(1, y+1):
            #     if (i, j) not in products:
        global unique_count
        unique_count += 1
        print(f"New one! Now at {unique_count} unique combinations.")
        helper(x, y)

    return remainders[(x,y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
