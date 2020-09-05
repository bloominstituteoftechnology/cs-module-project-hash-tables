class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """
        str_bytes = str(key).encode()
        total = 0
        for b in str_bytes:
            total += b

            total &= 0xFFFFFFFFFFFFFFFF
        return total

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        str_bytes = str(key).encode()
        total = 0
        for b in str_bytes:
            total += b

            total &= 0xFFFFFFFF
        return total

    def _hash_index(self, key):
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
        hashed_key = self._hash_index(key)
        new_linked_pair = HashTableEntry(key, value)

        node = self.storage[hashed_key]
        if node is None:
            self.storage[hashed_key] = new_linked_pair
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            prev.next = new_linked_pair

        else:
            node.value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        hashed_key = self._hash_index(key)

        node = self.storage[hashed_key]

        if node.key == key:
            self.storage[hashed_key] = node.next
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f"{key} was not found")
            return None
        prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        hashed_key = self._hash_index(key)

        node = self.storage[hashed_key]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        self.capacity = self.capacity * 2
        new_storage = [None] * self.capacity

        for i in range(len(self.storage)):
            node = self.storage[i]

            while node is not None:
                hashed_key = self._hash_index(node.key)
                new_storage[hashed_key] = node
                node = node.next
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")