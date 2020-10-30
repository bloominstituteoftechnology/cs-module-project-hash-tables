# Compute the Expensive Sequence

It's like the Fibonacci Sequence, but a lot more computationally
expensive and a lot less useful.

```
exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
```

`x`, `y`, and `z` are all greater than or equal to zero.

This will be tested on inputs as large as:

```
x = 150
y = 400
z = 800
```

Use a hashtable to make sure your solution completes before the universe
ends.

Hint: Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat n
ghcyr.

*In Python, a dict key can be any immutable type... including a
tuple.

(That's encrypted with ROT13--Google `rot13 decoder` to decode it if you
want the hint.)

--------------------------------------------------------------------------

What is this question asking me?

it looks like i will be given numbers x y z

xyz are equal to or greater than zero

I need to use a hash table to do something ???

Needs to be calculated before a certain time.

PSEUDOCODE

1.it looks like i will be given numbers x y z
def expensive_sequence(x, y, z):

____________________
# 0 1 1 2 3 5 8 13 21
​
# Memoization, caching
​
def fib(n):
	cache = {}/
​
	def fib_inner(n):
		if n <= 1:
			return n
​
		if n not in cache:  # if n's not a key in the cache dict
			cache[n] = fib_inner(n-1) + fib_inner(n-2)
​
		return cache[n]
​
	return fib_inner(n)
​
for i in range(95):
	print(f'{i}: {fib(i)}')

----------------------

def memoize(f):
        results = {}
        def helper(n):
            if n not in results:
                results[n] = f(n)
            return results[n]
        return helper

    @memoize
    def linear_combination(n):
        """ returns the tuple (i,j,k,l) satisfying
            n = i*1 + j*3 + k*9 + l*27      """
        weighs = (1,3,9,27)

        for factors in factors_set():
           sum = 0
           for i in range(len(factors)):
              sum += factors[i] * weighs[i]
           if sum == n:
              return factors 
-----------------

#Build an inverse square root lookup table

1 / sqrt(n)


inv_sqrt = {}
build a table

function that runs it
def build_lookup_table():

for i in range (1, 1000):
     inv_sqrt[1] = 1/ math.sqrt(i)

build_lookup_table()

print(inv_sqrt[4])
print(inv_sqrt[4.2])
print(inv_sqrt[22])


