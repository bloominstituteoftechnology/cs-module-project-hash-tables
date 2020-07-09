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
        self.capacity = max(MIN_CAPACITY, capacity)
        self.indices = [None] * self.capacity
        self.size = 0
        self.occupied_indices = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.indices)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.occupied_indices / self.capacity

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
        for char in key:
            hash = (hash * 33) + ord(char)
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
        # Compute index of key
        index = self.hash_index(key)
        # Go to the node corresponding to the hash
        node = self.indices[index]
        # Increment size
        self.size += 1
        # If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.indices[index] = HashTableEntry(key, value)
            # Increment count of non-null indices
            self.occupied_indices += 1
            # check load factor, if above 0.7, resize table to double it's current size
            if self.get_load_factor() >= 0.7:
                self.resize(self.capacity * 2)
            return
        # Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            # If key exists, update value, return
            if key == node.key:
                node.value = value
                return
            else:
                prev = node
                node = node.next
        # Add a new node at the end of the list with provided key/value
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Compute hash
        index = self.hash_index(key)
        node = self.indices[index]
        prev = None
        # Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # Key not found
            return None
        else:
            # The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.indices[index] = node.next  # May be None, or the next match
            else:
                prev.next = prev.next.next  # LinkedList delete by skipping over
            # Return the deleted result
            return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Compute hash
        index = self.hash_index(key)
        # Go to first node in list at bucket
        node = self.indices[index]
        # Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Store a copy of the current table
        curr_table = self.indices
        # Update capacity
        self.capacity = new_capacity
        # Create a new table at the new capacity
        self.indices = [None] * self.capacity
        #  Traverse the current table
        for i, _ in enumerate(curr_table):
            # Get the node at the current index
            node = curr_table[i]
            # If the node is not None
            if node is not None:
                # Traverse the linked list, hashing the values at each node into the new table
                curr_node = node
                while curr_node is not None:
                    self.put(curr_node.key, curr_node.value)
                    curr_node = curr_node.next
        return


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
    ht.put("line_12", "I changed the last line")
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
