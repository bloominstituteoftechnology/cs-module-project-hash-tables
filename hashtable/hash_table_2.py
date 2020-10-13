
new_list = [None] * 8

def my_hash(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b

    return total


# choose some big random number, usually prime
# loop over the bytes of our string, and do something weird
# return the weird result

# "something weird" mean with the bits, which you'll learn in computer architecture

def djb2(s):
    hash_var = 5381
    
    string_bytes = s.encode()

    for b in string_bytes:
        hash_var = ((hash_var << 5) + hash_var) + b

    return hash_var


# print(djb2("barn") % len(new_list))
# print(djb2("howdy") % len(new_list))

    # def djb2(self, key):
    #     hash = 5381
    #     for element in key:
    #         hash = (hash * 33) + ord(element)
    #     return hash

def fnv(s):
    FNV_offset_basis = 14695981039346656037 
    FNV_prime = 1099511628211 

    hashed_var = FNV_offset_basis

    string_bytes = s.encode()

    for b in string_bytes:
        hashed_var = hashed_var * FNV_prime
        hashed_var = hashed_var ^ b

    return hashed_var

# Why make a big hash if we are just going to shrink it by using modulo?



def put(key, value):
    hashed_key = djb2(key)

    idx = hashed_key % len(new_list)

    if new_list[idx] is not None:
        print(f"COLLISION: you are overwriting at {idx}")

    new_list[idx] = value

put("hello", "hello world")
put("howdy", "howdy world")

def get(key):
    hashed_key = djb2(key)

    idx = hashed_key % len(new_list)

    value = new_list[idx]
    return value

print(get("hello"))
print(get("howdy"))

def delete(key):
    # hash it
    hashed_key = djb2(key)
    # modulo to get the index
    idx = hashed_key % len(new_list)

    # go into the list and set to None
    new_list[idx] = None

# What happens if two different keys hash to the same index?
## called a collision
## we are currently overwriting!!

put("barn", "moo cow")
print(get("barn"))
print(get("howdy"))

# Detection: check if there's a value

# How to handle?
## Linked list! Put a chain there <-- we'll do this one
## Open addressing: linear probing
## Nested hash tables?

# an array full of Linked Lists
## node properties: key, value, next

# Index     List value
#  0         Node("barn", "moo cow") --> Node("howdy", "my new howdy value"") --> None
#  1         None
# 2          None
# 3          None
#  4         Node("hello", "hello world") --> None

put("howdy", "howdy world") # index 0 - collision

put("howdy", "my new howdy value")
# hash the key, modulo to get index, go to index
# 


# [Node("moo cow"), None, None, None, Node("hello world"), None]

# put with no collision: add a node, start of LL
# put with a collision: add a node to head or tail of the LL

get("hello")
## hash the key, modulo it to get index, go to index
## compare with the original key
## if key matches, return value

get("howdy")
## hash the key, modulo to get index, go to index
## compare with the original key
## if key matches, return value

get("super") # hashes/module to index 4
## iterate down LL
## if not found, return None

class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):
        # check if the key is already in the linked list
            # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next

        # if we reach the end of the list, it's not here! 
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node


    def update_or_else_insert_at_tail(self):
        # walk through and check if key is here
        # if not, make a new node and insert at tail
        pass

    def delete(self):
        pass

# Make a LL work with your HashTable
## put --> hash, get index, put a LL at the index
## get --> hash, get index, call the LL method to get the value (or None)

# What we talked about
# Put, get, delete
# Collisions
# How to handle with a LL
# LL operations, a little of how to make it work with our HashTable

# Hash Table
# 0 | A -> N -> O
# 1 | D -> G
# 2 | E -> P
# 3 | B -> H -> I -> J
# 4 | F -> Q
# 5 | R -> S -> T
# 6 | C -> K -> L -> M
# 7
get("A")

# Hash Table with load factor < 0.7
# 0 | A
# 1 | D
# 2 | E
# 3 | B 
# 4 | F -> R
# 5 |
# 6 |
# 7

# number_elements / 8 = 0.7
# number_elements / 5.6

# time complexity of perfectly loaded hash table?
# hash (constant time)
# modulo O(1)
# get head of LL: O(1)

# time complexity of an overloaded hash table?
get("J")
# hash
# modulo
# iterate down our LL

# we're approaching linear time
## worst case would be they all go to same index, in same "bucket"
## avoid with a good hash function
## but eventually we will overload

# Load Factor
# 20 / 8 = 2.5
# number of elements / number of slots

# 50 / 32 slots = 1.6
# load factor of 1.6

# What load factor tells us to resize?
## Rule of thumb: 0.7 load factor, resize
## if 0.2, resize down

# if load factor is 0.5, do we have a 50% chance of collision??
## TO BE CONTINUED

# How to fix??
## Resize!

# How to resize to a larger hash table?
## Double the size of the array

## (remember if a regular array runs out of memory, we just double size)

## Step 1: make a new array, double the size of the old one
## Step 2: iterate through old array, and iterate old linked lists
## Step 3: insert into new array, same way we did in the old array

### len(new_array) is bigger --> used with modulo, gives a different index

## When you put, or delete, check if you should resize up, or down

## Today's part of the project:
### collision resolution with chaining --> aka make a LL work with your hash table
### Resizing up
### Resizing down is a stretch goal