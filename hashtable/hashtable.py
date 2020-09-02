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
        self.capacity = MIN_CAPACITY
        self.count = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Return the length of the list you're using to hold the hashtable data.
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Return the load factor for this hash table.
        return self.count / self.capacity


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
        hash = 5381
        for element in key:
            hash = (hash * 33) + ord(element)
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
        # Store the value with the given key.
        index = self.hash_index(key)
        entry = HashTableEntry(key, value)
        storage = self.storage[index]
        self.count += 1

        # Hash collisions should be handled with Linked List Chaining.
        if storage:
            self.storage[index] = entry
            self.storage[index].next = storage
        else:
            self.storage[index] = entry


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Remove the value stored with the given key.
        if self.get(key):
            self.put(key, None)
            self.count -= 1
        # Print a warning if the key is not found.
        else:
            print("Key not foud")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Retrieve the value stored with the given key.
        index = self.hash_index(key)
        storage = self.storage[index]
        while storage:
            if storage.key == key:
                return storage.value
            storage = storage.next
        # Returns None if the key is not found.
        return None
    
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        load = self.get_load_factor()
        # When load factor increases above 0.7, 
        if load > 0.7:
            # automatically rehash the table to double its previous size.
            new_table = [None] * (new_capacity)
            old_table = self.storage
            self.storage = new_table
            # Update capacity to new balue
            self.capacity = new_capacity
            # for each slot in table:
            for entry in old_table:
		    # for each element in the linked list in that slot:
                cur = entry
                # PUT that element in new_table
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next
        # When load factor decreases below 0.2
        # down to a minimum of 8 slots.
        if load < 0.2 and new_capacity > 8:      
            # automatically rehash the table to half its previous size, 
            new_table = [None] * (new_capacity)
            old_table = self.storage
            self.storage = new_table
            # Update capacity to new value
            self.capacity = new_capacity
            # for each slot in table:
            for entry in old_table:
		    # for each element in the linked list in that slot:
                for element in entry:
		        # 	PUT that element in new_table
                    self.put(element.key, element.value)
        
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
