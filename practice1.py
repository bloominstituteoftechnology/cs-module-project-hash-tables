# What are hash tables good for?
# hash tables allows very fast lookup/search access
# --Memoization
#     -- cache system
#     -- do something hard once -- save forever
cache = {}
def fib(n):
  if n<=2:
    return n
  # if the result is in the cache - use it
  if n in cache:
    return cache[n]  
  #if the result is not in the cache
  # do the expensive calculations  
  result =  fib(n-1) + fib(n-2)
  #Store the results from the expensive calculations
  cache[n] = result
  return result

# print(fib(5))  
print(fib(50))
