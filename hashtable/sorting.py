# Is order in a hash table guaranteed? -> Python 3 has begun to preserve order. In Python 2 - no
# Hash functions scramble keys into unpredictable indecies
# Can't sort a dictionary, especially not hash tables in general
# Can sort a list based on it.


# goal: sort dictionary by keys
d = {
    "foo": 1,
    "bar": 99,
    "qux": 42
}

for pair in d.items():
    print(pair)
    
dict_list = list(d.items())

dict_list.sort()

# or sorted(dict_list) - returns a new list, without mutating the old list in place

# How could we sort reverse alphabetical? aka, descending
dict_list.sort(reverse=True)

# how to sort by value, not key
list(map(key = lambda pair: pair[1]))

# sort descending by value
dict_list.sort(key = lambda pair: pair[1], reverse=True)