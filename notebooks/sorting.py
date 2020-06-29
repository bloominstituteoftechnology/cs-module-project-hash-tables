# Let's sort a dictionary /hash table

dictionary = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(dictionary.items())
# Sort items ascending by key
items.sort()

print(f' Sort items ascending by key:', items)

print("+---------------------------------------------------------------------+")
# Sort items decending by key
items.sort(reverse=True)
print(f' Sorted items in deceding by key:', items)

print("+---------------------------------------------------------------------+")
print(f' Another way to print out our dictionaries:', dict(items))

#  Sort ascending by value
# writing our function:


def get_key(e):  # e is going to be the tuple
    # Return the thing that we want to sort by
    # we have sorted based on index [0]
    return e[0]


items.sort(key=get_key)
items.sort(key=get_key, reverse=True)
print("+---------------------------------------------------------------------+")
print(items)

# lambda function
# is an anonymous function.

items.sort(key=lambda e: [1])
print("+---------------------------------------------------------------------+")
print(f'Using lambda function:', items)
