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
        self.bucket = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Day 2
        pass

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Day 2
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Day 1
        # hash = 5381
        # byte_array = key.encode('utf-8')

        # for byte in byte_array:
        #     # the modulus keeps it 32-bit, python ints don't overflow
        #     hash = ((hash * 33) ^ byte) % 0x100000000

        # return hash

        hash = 5381
        for c in key:
            hash = (hash << 5) + hash + ord(c)
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
        # Day 1
        # index = self.hash_index(key)
        # print('INDEXES:', index)
        # self.bucket[index] = value
        # print(index)

        # Day 2

        # get the key index value by hashing the key with hash_index
        index = self.hash_index(key)
        # initialize an table entry using the key and the value
        new_node = HashTableEntry(key, value)
        # assign a current node to the node at the hash key position
        current_node = self.bucket[index]
        # check if the value at the hashed key/index in bucket is None
        # if it is place the node at this position
        if self.bucket[index] == None:
            print('in func index was None:', new_node.value)
            self.bucket[index] = new_node
            self.count += 1

        # else enter while loop to find the next none position then place
        # the node there.
        else:
            while current_node is not None:
                print("entered Loop")
                if current_node.next is None:
                    print('In Func While Loop:', new_node.value)
                    current_node.next = new_node
                    self.count += 1
                    return current_node
                else:
                    current_node = current_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Day 1
        # index = self.hash_index(key)
        # self.bucket[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        return self.bucket[index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


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

    # for i in ht.bucket:
    #     print('Storage Array: ', i.value, i.next, ht.count)

    print("")
