class HashTableEntry:
    """
    Linked List hash table key/value pair.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'
    
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=8):
        # Hash table can't have fewer than this many slots
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        num_slots = len(self.storage)
        return num_slots

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


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
        # Find position of key in hash table
        position = self.hash_index(key)
        
        # If hash table position is filled
        if self.storage[position] != None:
            # Create a HashTableEntry
            entry = self.storage[position]
            # While an entry exists
            while entry:
                # If our value is in our HashTableEntry, replace value
                if entry.key == key:
                    # Set the value of the entry to value being put
                    entry.value = value
                    # insertion complete
                    break
                elif entry.next == None:
                    # If arrived at the end of the HashTableEntry
                    # add new value
                    entry.next = HashTableEntry(key, value)
                    # insertion complete
                    break
                else:
                    entry = entry.next

        # If hash table position is empty, add entry
        else:
            self.storage[position] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Find the position in table where value exists given key
        position = self.hash_index(key)
        entry = self.storage[position]
        
        if self.storage[position] == None:
            return('There is no key & value at that position!')
        
        # If our hash table entry is a no-collision, one entry long case
        if entry.next == None:
            # Delete value
            if entry.key == key:
                entry.value = None
                return
            # Return error message if no slot is filled but with no hash table entry    
            else:
                return("Can't remove it if it doesn't exist!")
        
        # While there are multiple entries at that position of the hash table
        while entry:
            # base case of removing value
            if entry.key == key:
                entry.value = None
                return(f"Value for key '{key}' deleted.")
            # cycling through linked list of entries    
            entry = entry.next
        # Outlier case where we go through list of collided entries but no value were deleted
        return('There is no key of that value!')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get position and entry information for key
        position = self.hash_index(key)
        entry = self.storage[position]
        
        # Staged lookup value for get command
        lookup = None
        
        # While entry is not None
        while entry:
            # cycle 
            if entry.key == key:
                lookup = entry.value
                return lookup
            else:
                entry = entry.next
        return "Value not found."


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        new_storage = [None] * self.capacity
        
        for i in self.storage:
            if i != None:
                entry = i
                while entry:
                    key = entry.key
                    value = entry.value
                    pos = self.hash_index(key)
                    new_entry = new_storage[pos]
                    
                    if new_entry != None:
                        
                        while new_entry:
                            if new_entry.next != None:
                                new_entry = new_entry.next
                            else:
                                new_entry.next = HashTableEntry(key, value)
                                new_entry = None
                    else:
                        new_storage[pos] = HashTableEntry(key, value)
                        
                    entry = entry.next
        self.storage = new_storage



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
