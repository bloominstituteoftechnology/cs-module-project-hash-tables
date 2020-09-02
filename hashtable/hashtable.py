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
        self.HashTable = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """

        return len(self.HashTable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """

        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hashed_var = FNV_offset_basis
        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b

        return hashed_var

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        idx = self.hash_index(key)

        if self.HashTable[idx] is None:
            self.HashTable[idx] = HashTableEntry(key, value)
            self.size += 1
            return

        curr = self.HashTable[idx]
        self.HashTable[idx] = HashTableEntry(key, value)
        self.HashTable[idx].next = curr
        self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """

        idx = self.hash_index(key)
        current = self.HashTable[idx]
        prev = None

        while current:

            if current.key == key:

                if prev:
                    prev.next = current.next
                    self.size -= 1
                    return

                else:
                    self.HashTable[idx] = current.next
                    self.size -= 1

            prev = current
            current = current.next

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here

        idx = self.hash_index(key)
        node = self.HashTable[idx]

        while node is not None and node.key != key:

            node = node.next

        if node is None:
            return None

        else:
            return node.value

        # Get method for no collisions = Day # 1

        # index = self.hash_index(key)

        # return self.HashTable[index].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY

        prev_HashTable = self.HashTable
        self.capacity = new_capacity
        self.HashTable = [None] * new_capacity
        self.size = 0

        # Rehash all the values from prev_HashTable and mod them into new table
        for item in prev_HashTable:
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
