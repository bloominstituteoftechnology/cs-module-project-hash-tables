class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
            
        self.capacity = capacity
        self.table = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_offset_basis = 14695981039346656037
        bytes_representation = key.encode()
        for byte_of_data in bytes_representation:
            FNV_prime = 1099511628211
            FNV_offset_basis = FNV_offset_basis * FNV_prime
            FNV_offset_basis = FNV_offset_basis ^ byte_of_data
        
        hashValue = FNV_offset_basis
        return hashValue

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        
        indexForKey = self.hash_index(key)
        
        if self.table[indexForKey] is None: #no pairs found
            self.table[indexForKey] = HashTableEntry(key, value) #create new
        else: #pairs found
            pair = self.table[indexForKey]
            while pair is not None:
                if pair.key == key: #if exists
                    pair.value = value #update value
                    return
                if pair.next is None: #last
                    pair.next = HashTableEntry(key, value) #append new
                    return
                pair = pair.next #advance
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        
        indexForKey = self.hash_index(key)
        firstPair = True 
        pair = self.table[indexForKey]
        prevPair = None
        
        while pair is not None: #is there
            if pair.key == key: #found it
                if firstPair: #is head
                    if pair.next == None: #one pair
                        self.table[indexForKey] = None
                        pair = None
                    else: 
                        self.table[indexForKey] = pair.next #shift / cut out node from list
                        pair = None
                else: #inside linked list
                    if pair.next == None: #is last
                        prevPair.next = None
                        pair = None
                    else: 
                        prevPair.next = pair.next #shift / cut out node from list
                        pair = None
                return
            
            firstPair = False
            if pair.next == None:
                return 
            prevPair = pair
            pair = pair.next 
        
        
        
        
        
        # solution for list
#        if self.table[indexForKey] is None: #guard, has value
#            return
#        for index in range (0, len(self.table[indexForKey])):
#            if self.table[indexForKey][index].key == key:
#                self.table[indexForKey].pop(index)
#                return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        indexForKey = self.hash_index(key)
        pair = self.table[indexForKey]
        
        while pair is not None: #there is something
            if pair.key == key: #found it?
                return pair.value #return it
            pair = pair.next  #advance

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        old_capacity = self.capacity

        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for index in range(old_capacity):
            pair = old_table[index]
            while pair is not None:
                self.put(pair.key, pair.value)
                pair = pair.next 

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
