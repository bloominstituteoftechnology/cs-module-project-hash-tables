# Your code here
import random, math, time

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}
cache_pow = {}
cache_fact = {}
cache_intd = {}
cache_mod = {}
v = None


def slowfun(x, y):
     """
     Rewrite slowfun_too_slow() in here so that the program produces the same
     output, but completes quickly instead of taking ages to run.
     """
     # Your code here

     global v
     test_key = str(f'{x}{y}')


     if test_key in cache_pow:
          # print(f' Return from cache_pow cache')
          v = cache_pow[test_key]
     else:
          v = math.pow(x, y)
          cache_pow[test_key] = v
          # print(f' v pow CALC is {v} ')

     if test_key in cache_fact:
          # print(f' Return from cache_fact')
          v = cache_fact[test_key]
     else:
          v = math.factorial(v)
          cache_fact[test_key] = v
          # print(f' >>>> v fact CALC ')
     
     if test_key in cache_intd:
          v = cache_intd[test_key]
     else:
          v //= (x + y)
          cache_intd[test_key] = v

     if test_key in cache_mod:
          return cache_mod[test_key]
     else:
          v %= 982451653
          cache_mod[test_key] = v 
    
     return v
# Do not modify below this line!

t1 = time.time()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print(f' time is run test was {round(time.time() - t1, 3)}')
#49999: 12,5: 840852698
 # time is run test was 5.113    🔥🔥🔥🔥🔥🔥🔥

