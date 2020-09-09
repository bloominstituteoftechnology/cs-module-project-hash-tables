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
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        self.buckets = [None] * self.capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed_result = FNV_offset_basis
        key_bytes = key.encode()

        for byte in key_bytes:
            hashed_result = hashed_result * FNV_prime
            hashed_result = hashed_result ^ byte
        return hashed_result


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # make a variable equal to 5381
        hashed_result = 5381
        ## iterate over the bytes of our key
        key_bytes = key.encode()
        ## for each byte,
        for byte in key_bytes:
            ### shift the variable and add it, then add the byte
            hashed_result = ((hashed_result << 5) + hashed_result) + byte
        return hashed_result

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        idx = self.hash_index(key)

        new_node = HashTableEntry(key, value)
        current_node = self.buckets[idx]
        
        if current_node == None:
            self.buckets[idx] = new_node
            self.count += 1
        
        elif current_node is not None and current_node.key == key:
            self.buckets[idx].value = value
        
        elif current_node is not None:
            while current_node is not None:
                if current_node.next is None:
                    current_node.next = new_node
                    self.count += 1
                    return current_node
                elif current_node.next is not None and current_node.next.key == key:
                    current_node.next.value = value
                    return current_node.next
                else:
                    current_node = current_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        current_node = self.buckets[hashed_index]

        if current_node is None:
            return None

        if current_node.key == key:
            node_to_delete = current_node
            self.buckets[hashed_index] = node_to_delete.next
            node_to_delete.next = None

        else:
            while current_node is not None:
                if current_node.next.key == key and current_node.next.next is not None:
                    next_node = current_node.next
                    current_node.next = current_node.next.next
                    return next_node

                current_node = current_node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        current_node = self.buckets[hashed_index]

        if current_node is not None and current_node.key == key:
            return self.buckets[hashed_index].value

        else:
            while current_node is not None:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_bucket = [None] * new_capacity
        old_bucket = self.buckets

        self.buckets = new_bucket
        self.count = 0
        self.capacity = new_capacity

        current_index = 0
        while current_index < len(old_bucket):
            current_node = old_bucket[current_index]
            if current_node is not None:
                next_node = current_node.next
                current_node.next = None
                self.put(current_node.key, current_node.value)
                old_bucket[current_index] = next_node
            elif current_node is None:
                current_index += 1



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
