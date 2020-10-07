#meoization
#cache system
#do something once, save forever
cache = {}

def fib(n):
    if n <= 1:
        return n
    #if the result is in the cache
    if n in cache:
        return cache[n]

    #if the result is not in the cache
    #do the expensive calc
    result = fib(n-1) + fib(n-2) #O(2^N)
    #store the result
    cache[n] = result

    return result
#0, 1, 1
print(fib(5))
print(fib(40))