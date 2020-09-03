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

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity


    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        hash = 14695981039346656037 # offset_basis
        for s in key:
            hash = hash * 1099511628211 # FNV_prime
            hash = hash ^ ord(s)
        return hash % len(self.array)


    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xffffffff % self.capacity


    def hash_index(self, key):
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    # Ignores Collisions (will overwrite any existing values at the calculated index)
    def put(self, key, value):
        index = self.hash_index(key)
        if self.array[index] is not None:
            print(f"Collision Warning: overwriting value: '{self.array[index]}', with value: '{value}'")
        self.array[index] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if index is None:
            print(f"Warning: Tried to delete a value from HashTable but no value exists for key: '{key}'")
        self.array[index] = None


    def get(self, key):
        index = self.hash_index(key)
        return self.array[index]


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
