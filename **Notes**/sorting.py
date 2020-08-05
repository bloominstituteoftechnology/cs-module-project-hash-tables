
# If you iterate across, or print a hash table, will the items be in the order in which you put them?
## No
## Why not?
### sets and objects are not ordered
## Unlike lists/arrays

## Python dictionaries do preserve order


# Sorting
my_list = [99, 45, 12, 67, 23, 5]
# sorted, list.sort()

# basically hash table with methods added
mydict = {"foo": 11, "bar": 42, "qux": 99}

# it doesn't make sense to sort a hash table
# sort a list based on the dictionary

# lambda functions are much like anonymous functions in JS
# JS: (x) => x[1] in js

# sorted takes key=lambda, uses what the anonymous function returns to sort

# use lambda function to sort by value
# sorted(my_items, key=lambda x: x[1])

my_dict_items = list(mydict.items())

# sort by value
my_dict_items.sort(key=lambda x: x[1])

# sort by value, descending order
my_dict_items.sort(key=lambda x: x[1], reverse=True)
