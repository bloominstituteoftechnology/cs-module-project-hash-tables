# Let's sort a dictionary/hash table

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

print(d.values())
items = list(d.items())

# Sort ascending by key
items.sort()

print(items)

# Sort decending by key
items.sort(reverse=True)

print(items)

# Sort ascending by value

"""
def get_key(e):  # e is going to be the tuple
    # Return the thing that we want to sort by
    return e[1]

items.sort(key=get_key)
"""
items.sort(key=lambda e: e[1])

print(items)

