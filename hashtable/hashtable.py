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

        self.table = [None] * capacity
        self.capacity = capacity

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

        hash = 14695981039346656037 # FNV_offset_basis
        bytes_representation = key.encode()
        for byte_of_data in bytes_representation:
            hash = hash * 1099511628211 # FNV_prime
            hash = hash ^ byte_of_data

        return hash 



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
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        if self.table[index] == None:
            self.table[index] = HashTableEntry(key, value)
        else:
            pos = self.table[index]
            while pos != None:
                if pos.key == key:
                    pos.value = value
                    return
                if pos.next == None:
                    pos.next = HashTableEntry(key, value)
                    return 
                pos = pos.next 

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        firstPosition = True 

        priorPos = None
        pos = self.table[index]
        while pos != None:
            if pos.key == key:
                if firstPosition:
                    if pos.next == None:
                        self.table[index] = None
                        pos = None
                    else: 
                        self.table[index] = pos.next
                        pos = None
                else: 
                    if pos.next == None:
                        priorPos.next = None
                        pos = None
                    else: 
                        priorPos.next = pos.next
                        pos = None
                return
            
            firstPosition = False
            if pos.next == None:
                return 
            priorPos = pos
            pos = pos.next 

        print(f"Warning: Value not found at key: {index}")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        pos = self.table[index]
        while pos != None:
            if pos.key == key:
                return pos.value
            pos = pos.next 

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
            pos = old_table[index]
            while pos != None:
                self.put(pos.key, pos.value)
                pos = pos.next 



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
