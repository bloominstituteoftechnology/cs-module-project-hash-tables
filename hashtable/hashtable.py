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
        # Your code here
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
            self.storage = [None] * self.capacity
        else:
            print(f"Error: provided capactity is insufficient. Initializing with minimum capacity of {MIN_CAPACITY}.")
            self.capacity = MIN_CAPACITY
            self.storage = [None] * self.capacity
        self.stored_keys = 0
        self.load_factor = 0.7


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        fnv_prime = 0x00000100000001B3
        hash_int = 0xcbf29ce484222325

        hash_value = hash_int
        for char in key:
            hash_value *= fnv_prime
            hash_value ^ ord(char)
        return hash_value

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash_int = 5381
        hash_value = 0

        for char in key:
            hash_value = (hash_value * 33) + ord(char)
        return hash_value


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
        # Your code here
        if self.stored_keys / self.capacity > self.load_factor:
            self.resize(self.capacity * 2)
        target_index = self.hash_index(key)
        entry = self.storage[target_index]
        if not entry:
            self.storage[target_index] = HashTableEntry(key, value)
        else:
            previous_entry = None
            while entry:
                if entry.key == key:
                    entry.value = value
                    return
                previous_entry = entry
                entry = entry.next

            entry = HashTableEntry(key, value)
            previous_entry.next = entry
        self.stored_keys += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        target_index = self.hash_index(key)
        entry = self.storage[target_index]
        if not entry:
            print("Key not found. Key not found!")
            raise KeyError
        else:
            previous_entry = None
            while entry:
                if entry.key == key:
                    if previous_entry:
                        # previous_entry.next = entry.next
                        entry.value = None
                        return
                    else:
                        entry.value = None
                        return
                previous_entry = entry
                entry = entry.next
            print("Key not found. Key not found!")
            raise KeyError

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        target_index = self.hash_index(key)
        entry = self.storage[target_index]
        if entry:
            while entry:
                if entry.key == key:
                    return entry.value
                entry = entry.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old_storage = self.storage
        self.storage = [None] * self.capacity

        for entry in old_storage:
            while entry:
                self.put(entry.key, entry.value)
                entry = entry.next



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
