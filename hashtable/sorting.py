
# does a hash table preserve order?

"""
hash_table = HashTable()

hash_table.storage = [Node('key3', 'v3'), None, None, Node('key1', 'v1')]

hash_table.put('key1', 'v1')
hash_table.put('key2', 'v2')
hash_table.put('key3', 'v3')

hash_table.storage.sort()

hash_table.get('key1')
"""

# hash the key, get the index, looks there...????

arr = [1, 2, 3]
arr.append(1)
arr.append(2)
arr.append(3)

# why doesn't a hash table keep things in order, the way an array does?
# the hash function takes the key and returns a random index

# sets, dictionaries, object or hash maps

# can you sort a hash table (or dictionary/object/hash map)?
## go to the index, sort the linked list?

arr.sort()

# in Python, what if we got a list based on the dictionary?
my_dict = {
    'a': '1',
    'f00': 'izzy',
    'qux': 'bar',
}
# a list-like object - actually an iterator
my_dict.items()

dict_list = list(my_dict.items())

# sort by default goes in ascending order, aka normal alphabetical
# also by default uses the first item in each tuple to sort

dict_list.sort(reverse=True)

print(dict_list)

# print in ascending order, sorted by value
dict_list.sort(key=lambda tuple_pair: tuple_pair[1])
print(dict_list)

"""
[('a', 1), ('f00', 'bar'), ('qux', 'izzy')]


JS
x => x * x

lambda x, y: x * y

HOF: a function that takes a function
in functional programming (FP), we don't work in place
Instead always returns a new data structure

"pure function" has no side effects

map(lambda x: x * 2, [1, 2, 3, 4])
<map object at 0x10a5f8e10>
list(map(lambda x: x * 2, [1, 2, 3, 4]))
[2, 4, 6, 8]
"""