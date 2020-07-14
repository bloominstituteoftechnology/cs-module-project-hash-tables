# Big Ideas: use all the info you can to scramble stuff, even the bits
# 

def djb2(key):  
    hash = 5381
    for c in key:
        hash = (hash * 33) + ord(c)
    return hash

hash_table = [None] * 8

#data structure to store key/value
class HashTableItem:
    __init__(self, key, value, next = None):
        self.key
        self.value
        self.next = next


def my_hash(s):
    s_utf8 = s.encode()
    
    total = 0
    for c in s_utf8:
        total += c
    return total

def put(key, value):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)    
    hash_table[index] = HashTableItem(key, value)
    
    #print a warning if collision happens
    if hash_table[index] != None:
        print("OMG! THING OF THE DATA¡¡")
    
def get(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
    table_item = hash_table[index]
    return table_item.value

def delete(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
    hash_table[index] = None

put("hello", "hello world")
put("olleh", "we didn't start the fire")


print(hash_table)
# print(get("hello"))

# delete("hello")
# print(hash_table)


# put in a surrounding/different index - example of an open index
# linear probing: find the next avaliable index and put it there - example of an open index
# cuckoo probing: 
# double hashing: hash the hash and  get a different index
# disallow it


# chaining => our solution. Combine 2 data structures to make a new data structure. Have an array of linked lists

'''
Index    Chain (linked list)
-----    ------------------
0        ("qrx", 54) -> None
1        ("baz", 38) -> ("foo", 42) -> None
2        ("bar", 99) -> None
3        -> None
4        -> None


put("foo", 42) # hashed to index 1
put("bar", 99) # hashed to index 2
put("baz", 38) # hashed to index 1 !COLLISION!
put("qrx", 54) # hashed to zero

get("qrx") => finds it at index 0 no problem
get("foo") => have to traverse the list at index 1. Need to store the key and value together.
get("fred") => hashed to 0 ---> Nothing there ---> return None

delete("baz") => have to have the pointer point to .next
'''

# how to make the linked list work with our hash table??
# insert a linked list into the hash table, when you add something
# hash table main data structure : [LL, LL, None, LL, None, None]
# ensure each node has a key and a value
# change methods to use keys instead of values, where necessary
# write a new method insert_or_overwrite 
# search for the key, if found, overwrite
# if not, create a new node



# Generic ListNode and LinkedList
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, value):
        current = self.head
        
        while current is not None:
            if current.value == value:
                return current
            current = current.next
            
        return None
    
    def insert_at_tail(self, value):
        node = ListNode(value)
        
        #if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head
            
            while current.next is not None:
                current = current.next
                
            current.next = node
    
    def remove(self, value):
        current = self.head
        # if there is no head
        if current is None:
            return None
        
        #when trying to remove the head
        if current.value == value:
            self.head = current.next
            return current
        
        #when trying to remove something else
        else:
            previous = current
            current = current.next
            
            while current is not None:
                if current.value == value: #found it
                    previous.next = current.next # cut current out
                    return current # return deleted node
                else:
                    previous = current
                    current = current.next
            return None
            
                
'''
This is an overloaded hash table:
0     A  -> F
1     B  -> G  -> K  -> L
2     C  -> H
3     D  -> I  -> M  -> 0
4     E  -> J  -> P

get(A) - Jumps to 0, returns that

How do we know when to increase a hash table?
Hash Table Load Factor:
number of things put in / length of array

15/5 = 3

Want to keep the load factor to < 0.7 aka 70%
How do we resize??
make a new array, with DOUBLE the capacity, to reduce how often we need to do this

0  A
1  C
2
3
4  D -> F
5
6  B
7  E
8
9

How do you keep track of how many items inserted into hash?
Keep a counter, every time you insert
If you do a put/overwrite - that doesn't count

How do you shrink your hash based on the load factor?
When you delete things, you need to update the counter
If load factor is < 0.2 aka 20%, rehash! => Stretch goal
Make a new array at half the size, but do not have below 8 items.
'''     
                    
        