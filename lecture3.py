# 0 1 1 2 3 5 8 13 21
# memorization, caching
'''
cache = {}
def fib(n):
    if n <= 1:
        return n
    if n not in cache:  # if n's not a key in the cache dict
        cache[n] = fib(n-1) + fib(n-2)


    return cache[n]

for i in range(2000):
    print(f'{i}: {fib(i)}')
'''


'''

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2,
}

items = list(d.items())

# sort ascending by key
items.sort()

for i in items:
    print(f'{i[0]}: {i[1]}')

print('ending of ascending by key')

# sort by ascending value

def keyfunc(e):
    return e[1]
items.sort(key=keyfunc)

for i in items:
    print(f'{i[0]}: {i[1]}')

'''

def letter_count(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts
print(letter_count("aabbcaacb"))