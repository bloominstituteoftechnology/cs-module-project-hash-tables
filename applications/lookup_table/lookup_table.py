import random, math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """    
    products = {}
    factorials = {}
    quotients = {}
    remainders = {}
    
    def helper(a, b):
        # products[(a, b)] = math.pow(a, b)
        build_products(a, b)
        # factorials[a, b] = math.factorial(products[a, b])
        build_factorials(products[(a, b)])
        quotients[a, b] = factorials[products[(a, b)]] // (a + b)
        remainders[a, b] =  quotients[a, b] % 982451653

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


    if (x, y) not in products:
        for i in range(1, x+1):
            for j in range(1, y+1):
                if (i, j) not in products:
                    helper(i, j)

    return remainders[(x,y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
