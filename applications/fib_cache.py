# 0 1 1 2 3 5 8 13 21 34 55

# Memoization, "caching"
# Top-Down Dynamic Programming

cache = {}

def fib(n):
	if n <= 1:
		return n

	if n not in cache:
		cache[n] = fib(n-1) + fib(n-2)

	return cache[n]

for i in range(1000000):
	print(f"{i}: {fib(i)}")
