## Fibonacci Sequence

```py
# 0 1 1 2 3 5 8 13 21 34

cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]
```

## Sorting

```py
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())

# for t in d.items():
#     print(t)

print(items)

items.sort() #> sorts tuples in order by key (alphabetically)

print(items)

# Sort by value
# def fun1(e):
#     return e[1]

# items.sort(key=fun1)
items.sort(key=lambda e: e[1])

print(items)
```