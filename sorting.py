
# Is order in a hash table guaranteed?
my_list = []
my_list.append(3)
my_list.append(2)
my_list.append(1)

my_dict = {}

my_dict['key1'] = 1
my_dict['key2'] = 2
my_dict['key3'] = 3
my_dict['key4'] = 4

# {'key2', 'key4', 'key3': 3, 'key1'}

# Why not?
## Hash function scrambles keys to unpredictable indices


# goal: sort dictionary keys

d = {
    "foo": 1,
    "bar": 99,
    "qux": 42,
}

# Can't sort a dictionary, especially not hash tables in general
# But we could sort a list based on it!

for pair in d.items():
    print(pair)

dict_list = list(d.items())

dict_list.sort()

# or sorted(dict_list) - return a new list, not mutate the old list in place

# How could we sort reverse alphabetical? aka, descending
dict_list.sort(reverse=True)

# how to sort by value, not by key?
# (x, y) => x + 1
dict_list.sort(key=lambda pair: pair[1])

# sort descending by value, using Python's lambda functions
dict_list.sort(key=lambda pair: pair[1], reverse=True)