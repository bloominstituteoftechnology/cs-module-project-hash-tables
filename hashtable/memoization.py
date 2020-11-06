
# memoization, closely related to dynamic programming
## DP: top down, break the problem up as you
## reuse previous results

## key is what you have, value is what you calculate


# fibonacci sequence
## a function that returns the n-th item in the fibonacci sequence
## golden proportion

## 0 1 1 2 3 5 8 13 21 34 55 89
### Kanban board: card holds a feature, "make this button"
### 1 2 3 5 8 13 21 

# let's do it recursively

# need base case
# progress toward base case

cache = {}
def fib(n):
    if n == 0 or n == 1:
        return n

    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib(n - 1) + fib(n - 2)

        return cache[n]

print(fib(3)) # should be 2
print(fib(6)) # should be 8
print(fib(11)) # should be 89
print(fib(1050))