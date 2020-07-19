# 0, 1, 1, 2, 3, 5, 8, 13

#recursive functions require:
# base case
# move towards the base case
# function has to call itself

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tiny_recurse(n):
    if n <= 1:
        return n
    return tiny_recurse(n - 1)


cache = {}
def slow_fibonacci(n):
    if n <= 1:
        return n
    
    if n not in cache:
        cache[n] = slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    
    return cache[n]
    
    # use a cache!
    # Memoizing = storing the result as we go
    # Dynamic programming
    
