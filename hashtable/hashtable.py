class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def get_next(self):
        return self.next

    def set_next(self, entry):
        self.next = entry

    def set_value(self, value):
        self.value = value

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
        self.capacity = capacity
        self.table = [None] * capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
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
        # Your code here
        str_key = str(key).encode()
        hash_value = 5381
        for s in str_key:
            hash_value = ((hash_value << 5) + hash_value) + s

        return (hash_value & 0xffffffff)


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
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
        table_entry = HashTableEntry(key, value)
        self.count += 1
        if self.table[index] == None:
            self.table[index] = table_entry
        else:
            current_node = self.table[index]
            while current_node != None:
                if current_node.get_key() == key:
                    current_node.set_value(value)
                    return
                elif current_node.get_next() == None:
                    current_node.set_next(table_entry)

                current_node = current_node.get_next()

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.table[index]
        prev_node = None
        while current_node != None:
            if current_node.get_key() == key:
                self.count -= 1
                if prev_node == None:
                    current_node.set_value(None)
                else:
                    prev_node.set_next(current_node.get_next())

            prev_node = current_node
            current_node = current_node.get_next()

        if self.get_load_factor() < 0.2:
            new_capacity = self.capacity // 2
            if new_capacity < MIN_CAPACITY:
                self.resize(MIN_CAPACITY)
            else:
                self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.table[index]
        while current_node != None:
            if current_node.get_key() == key:
                return current_node.get_value()
            current_node = current_node.get_next()
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        prev_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for index in range(len(prev_table)):
            current_node = prev_table[index]
            while current_node != None:
                self.put(current_node.get_key(), current_node.get_value())
                current_node = current_node.get_next()



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