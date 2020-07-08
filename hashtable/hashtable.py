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
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.num_items = 0
        self.load_factor = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return self.load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_INIT = 0xcbf29ce484222325
        FNV_PRIME = 0x100000001b3

        hash = FNV_INIT
        for c in key:
            hash = hash * FNV_PRIME % 2**64
            hash = hash ^ ord(c)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash << 5) + hash + ord(c)
            hash = hash & 0xFFFFFFFF
        return hash

    def update_load_factor(self):
        """
        Calculate and set the load factor.
        """
        self.load_factor = self.num_items / self.capacity

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key, value)
            self.num_items += 1
        else:
            node = self.storage[index]
            while node.key != key and node.next is not None:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = HashTableEntry(key, value)
                self.num_items += 1
        self.update_load_factor()
        if self.load_factor > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            node = self.storage[index]
            prev = None
            while node.key != key and node.next is not None:
                prev = node
                node = node.next
            if node.key == key:
                if prev is None:
                    self.storage[index] = node.next
                else:
                    prev.next = node.next
                self.num_items -= 1
                self.update_load_factor()
                if self.load_factor < 0.2 and self.capacity >= 16:
                    self.resize(self.capacity // 2)
                return node.value
            else:
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            node = self.storage[index]
            while node.key != key and node.next is not None:
                node = node.next
            if node.key == key:
                return node.value
            else:
                return None

    def resize(self, new_capacity=None):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        old_storage = self.storage

        if new_capacity is None:
            new_capacity = len(self.storage) * 2

        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        for node in old_storage:
            while node is not None:
                self.put(node.key, node.value)
                self.num_items -= 1  # Not a new item.
                node = node.next

        self.update_load_factor()


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
