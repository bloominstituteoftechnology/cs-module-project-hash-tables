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
        if capacity > MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        self.array = [None] * capacity

        self.entries = 0

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
        return self.entries / self.get_num_slots()



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        #Values pulled from Wikipedia
        prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis
        for char in key:
            hash = hash ^ ord(char) #XOR is defined by a carat
            hash = hash * prime
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
        entry = HashTableEntry(key, value)
        if self.array[index] is None:
            self.array[index] = entry
            self.entries += 1
            return
        else: # Colliding.
            prev = None
            current = self.array[index]
            while current:
                if current.key == key:  # Overwrite
                    current.value = value
                    return
                prev = current
                current = current.next
            prev.next = entry
            self.entries += 1
            return


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.array[index]
        prev = None
        while current:
            if current.key == key:
                if prev: #There is a node before this one. Works regardless if next is None or not.
                    prev.next = current.next
                    self.entries -= 1
                    return
                else: #Previous is None, may or may not be a node after this.
                    self.array[index] = current.next
                    self.entries -= 1
                    return
            prev = current
            current = current.next
        return None





    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current = self.array[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_array = self.array
        self.capacity = new_capacity
        self.array = [None] * new_capacity
        self.entries = 0

        #Rehashing
        for item in old_array:
            current = item
            while current:
                self.put(current.key, current.value)
                current = current.next





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
