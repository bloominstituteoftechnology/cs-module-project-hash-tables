class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
# [key: value] and next to search next value 

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        self.capacity = capacity
        self.hash_data = [None] * capacity
        self.total = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.total / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        key_encoded = key.encode()
        hash = 5381
        for k in key_encoded:
            hash = ((hash << 5) + hash) + k ; # same as hash * 33 + byte
            hash &= 0xffffffff
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # we are making new entry and link it to that.
        index = self.hash_index(key)
        cur_entry = self.hash_data[index]

         
        while cur_entry is not None:
            if cur_entry.key == key:
                cur_entry.value = value
                return

            cur_entry = cur_entry.next

        new_entry = HashTableEntry(key, value)
        new_entry.next = self.hash_data[index]
        self.hash_data[index] = new_entry
        self.total += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.hash_data[index] = None

        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        currentData = self.hash_data[index]

        while currentData is not None:
            if currentData.key == key:
                return currentData.value 
        
            currentData = currentData.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

#Collision resolution by chaining
"""
1. Make our array of slots into an array of linked lists.
2. Each Linked list node is HashTableEntry.

PUT:

Slot
Index   Chain  (Linked List)
if not found add in those tables
0 -> None
1 -> HashTableEntry{Foo:12} -> None
2 {baz:999} -> {bar:30} -> None
3-> None

put("foo", 12) # hashes to 1
put("bar", 20) # hashes to 2
put("baz", 999) # hashes to 2 -- collision. 
put("bar", 50) # hashes to 2 -- collision. 


1. Figure out the index that holds this thing, in this case 1
2. Search the linked list to see if the key is there.
2a. if the key is there, overwrite the value, if the key already exists
2b. if not there, create a new HashTableEntry and insert it in the List.


GET:

1. Figure out the index for the key
2. Search the linked list at the index for the hastableentry that matches they key 
3. Return the value for the entry, or None if not found.


DELETE:
1. Figure out the index ffor the key 
2. Search the linked list at the index for the hashTableEntry that matches the key
2a. If found, delete the entry from the linked list---return the valuie
2b, if not found, then return none
"""

""" Hashh table load factor

1. Metric to indicate how overfull the hashtable is
w
O(1) hash table:

0 | -> D
1 | -> h
2 | -> A
3 | -> C
4 | -> G
5 | -> B
6 | -> E
7 | -> D

0 | -> D
1 | -> h -> R -> X -> Y
2 | -> A
3 | -> C -> J -> L -> N -> Z
4 | -> G
5 | -> B -> O 1 -> 2
6 | -> E
7 | -> D



how do we knoew when to resize the hash table?

load factor = number of elements stored in the hastable / number of slots.
8 / 8 = 1.0
16/ 8 = 2.0

if the load factor is over 0.7, grow the table (performance starts degrading.)
if the load factor is under 0.2, shrink the table (down to some minimum)
grow the table: double the size
shrink the table: halve the size.

When you PUT:
if the load factor > 0.7
create new  array with double size of the old one 

"""