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

---

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

---

## Sorting II

```py
def letter_count(s):

    d = {}

    for c in s:
        if c.isspace():
            continue

        c = c.lower()

        if c not in d:
            d[c] = 0

        d[c] += 1

    return d

def print_sorted_letter_count(s):
    
    d = letter_count(s)

    items = list(d.items())

    items.sort(key=lambda e: e[1], reverse=True)

    for i in items:
        print(f"{i[0]}: {i[1]}")

print_sorted_letter_count("hello")
```
output:
```sh
l: 2
h: 1
e: 1
o: 1
```

---

## Ceaser Cipher

```py
# Ceaser Cipher

# Hash tables as a map between data values

"""
GOATS
JEHFN
"""

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}

for k,v in encode_table.items():
    decode_table[v] = k

def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

def decode(s):
    r = ""

    for c in s:
        r += decode_table[c]

    return r

e = encode("GOATS")
print(e)
print(decode(e))
```
output:
```sh
JEHFN
GOATS
```