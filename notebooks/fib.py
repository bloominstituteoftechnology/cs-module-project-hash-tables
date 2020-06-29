# 0 1 1 2 3 5 8 13 21....
# starts off with 0:1
# our base case
# fibonacci sequence

# 2n

# Memoization, top-down dynamic programming

cache = {}


def fib(n):
    # base case
    if n <= 1:
        return n
    # common case
    # if n is not a key in the cache
    # will add it
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2) + fib(n-2)
    return cache[n]

    # return fib(n-1) + fib(n-2)


# :3 is our field input
for i in range(95):
    print(f'{i:3} {fib(i)}')

"""
Our calls:

fib(30) = fib(29) + fib(28)
fib(29) = fib(28) + fib(27)
fib(28) = fib(27) + fib(26)
fib(28) = fib(27) + fib(26)
fib(27) = fib(26) + fib(25)
fib(26) = fib(25) + fib(24)

"""
