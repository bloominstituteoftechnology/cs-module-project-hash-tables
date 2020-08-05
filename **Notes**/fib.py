
# fibonacci sequence?
## the next number is sum of previous 2
## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# base case
# progress toward the base case
# call itself

# memoize in a cache?
cache = {}

def fib(n):
    # base case
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

# O(2^n)
# O(times_calls_self^n)

print(fib(77))

# memoization
# dynamic programming