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
    # updated from class
    def __init__(self, capacity):
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
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # number of items divided by number of buckets
        # try to keep between 20 - 70%
        return self.count / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # FNV1 parameters
        offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        # hash function, alternate version
        hash = offset_basis
        key_bytes = key.encode()
        # for each byte of data to be hashed
        for byte in key_bytes:
            hash = hash * FNV_prime
            hash = hash ^ byte
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # make hash == to 5381
        hash = 5381
        # encode
        byte_array = key.encode()
        for arr in byte_array:
            # hash math
            hash = ((hash << 5) + arr)
            # hash = ((hash * 33) + arr)
        return hash


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
        index = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        existing_node = self.table[index]
        self.count += 1
        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    existing_node.value = value
                    return
                last_node = existing_node
                existing_node = existing_node.next
            last_node.next = new_node
        else:
            self.table[index] = new_node
        if self.get_load_factor() > 0.7:
            return self.resize(self.capacity * 2)


        # HANDLING COLLISSIONS WITH A LINKED LIST

        # if there's None, just make a node. That's the LL head
        ## increment your load by 1

        # if there's already a node, iterate down and check keys
        # if you find the key, overwrite the value
        ## don't increment the load
        ### stop incrementing and return

        # if you reach the end, then add a node at the head or the tail
        ## increment the load by 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        delete_at_index = self.hash_index(key)
        existing_node = self.table[delete_at_index]

        if existing_node:
            self.count -= 1
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    if last_node:
                        last_node.next = existing_node.next
                    else:
                        self.table[delete_at_index] = existing_node.next
                last_node = existing_node
                existing_node = existing_node.next
        if self.get_load_factor() < 0.2:
            return self.resize(int(self.capacity / 2))
        else:
            print("Key not found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        existing_node = self.table[index]
        if existing_node:
            while existing_node:
                if existing_node.key == key:
                    return existing_node.value
                existing_node = existing_node.next
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if new_capacity > 8:
            self.capacity = new_capacity
        else:
            self.capacity = 8
        old_array = self.table
        self.table = [None] * self.capacity
        old_size = self.count

        current_node = None

        for entry in old_array:
            current_node = entry
            while current_node != None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next
        self.count = old_size


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
