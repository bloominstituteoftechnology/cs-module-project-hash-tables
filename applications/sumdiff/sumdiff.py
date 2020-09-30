"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
cache = {}
def sum_diff(q):
    new_arr = []
    for i in q:
        new_arr.append(f(i))
    
    f(1) + f(1) = f(12) - f(7) 
    if n not in cache:
    	cache[n] = fib(n-1) + fib(n-2)

	return cache[n]
