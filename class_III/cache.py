# 0 1 1 2 3 5 8 13 21 34

cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]

for i in range(100):
    print(f"{i:3}: {fib(i)}") #> Runs quickly, but still O(n)!
