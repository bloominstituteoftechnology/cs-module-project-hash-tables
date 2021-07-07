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