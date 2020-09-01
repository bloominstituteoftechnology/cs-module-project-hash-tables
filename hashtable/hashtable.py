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
        self.capacity = capacity
        self.size = 0
        if capacity >= MIN_CAPACITY:
            self.storage = [None] * self.capacity
        else:
            print(f"You must pick a capacity larger than {MIN_CAPACITY}.  Capacity set to {MIN_CAPACITY}.")
            self.storage = [None] * MIN_CAPACITY
        

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
        return self.size/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hval = 5381
        for s in key:
            hval = (hval * 33) + ord(s)
            return hval


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def get_index(self, key):
        index_value = self.fnv1(key)
        index_value %= len(self.storage)

        return index_value

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # index = self.get_index(key)
        # self.storage[index] = value

        index = self.hash_index(key)
        
        if (self.storage[index] == None):
            self.storage[index] = HashTableEntry(key, value)
            self.size += 1
        else:
            current_entry = self.storage[index]
            while current_entry.next != None and current_entry.key != key:
                current_entry = current_entry.next
            if current_entry.key == key:
                current_entry.value = value
            else:
                new_entry = HashTableEntry(key, value)
                new_entry.next = self.storage[index]
                self.storage[index] = new_entry
                self.size += 1

        if self.get_load_factor() > .7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # index = self.get_index(key)
        # self.storage[index] = None

        index = self.hash_index(key)
        if self.storage[index].key == key:
            if self.storage[index].next == None:
                self.storage[index] = None
                self.size -= 1
            else:
                new_head = self.storage[index].next
                self.storage[index].next = None
                self.storage[index] = new_head
                self.size -= 1
        else:
            if self.storage[index] == None:
                return None
            else:
                current_value = self.storage[index]
                previous_value == None
                while current_value.next is not None and current_value.key != key:
                    previous_value = current_value
                    current_value = current_value.next
                if current_value.key == key:
                    previous_value.next = current_value.next
                    self.size -= 1
                    return current_value
                else:
                    return None
        if self.get_load_factor() < .2:
            if self.capacity/2 > MIN_CAPACITY:
                self.resize(self.capacity/2)
            elif self.capacity > MIN_CAPACITY:
                self.resize(MIN_CAPACITY)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.get_index(key)
        # return self.storage[index]
        index = self.hash_index(key)
        if self.storage[index] is not None and self.storage[index].key == key:
            return self.storage[index].value
        elif self.storage[index] is None:
            return None
        else: 
            while self.storage[index].next != None and self.storage[index].key != key:
                self.storage[index] = self.storage[index].next
            if self.storage[index] == None:
                return None
            else:
                return self.storage[index].value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.storage[:]
        old_capacity = self.capacity
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for index in range(0 , old_capacity):
            if old_table[index] is not None:
                current_entry = old_table[index]
                self.put(current_entry.key, current_entry.value)



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
