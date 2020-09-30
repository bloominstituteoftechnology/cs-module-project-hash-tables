# 0 1 1 2 3 5 8 13 21 ...

# Memoization, top-down dynamic programming

cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache:   # if n is not a key in the cache
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

for i in range(95):
    print(f'{i:3} {fib(i)}')

"""
fib(30) = fib(29) + fib(28)
fib(29) = fib(28) + fib(27)
fib(28) = fib(27) + fib(26)
.
.
.
fib(1) = 1  base case
"""
