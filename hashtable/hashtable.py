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
        self.capacity = capacity
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.hash_array = capacity * [None]
        self.increment = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        print('Capacity is: ', self.capacity)
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.increment / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
    # source https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        # Your code here
        v1Prime = 1099511628211
        v1OSBasis = 14695981039346656037
        hash_id = v1OSBasis
        enc_key = key.encode()
        # for each byte_of_data to be hashed
    #     hash := hash × FNV_prime
    #     hash := hash XOR byte_of_data

    # return hash
        for byte in enc_key:
            hash_id = hash_id * v1Prime
            hash_id = hash_id ^ v1Prime
        return hash_id

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for byte in key:
            hash = hash * 33 + ord(byte)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity

        # hash_val = self.fnv1[key]
        # index = hash_val % len(self.hash_array)
        # return index

        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index = self.hash_index(key)
        # self.hash_array[index] = (key, value)
        hashIndex = self.hash_index(key)

        # append to empty slot
        # if not hash_array[self.hash_index(key)]
        if not self.hash_array[hashIndex]:
            self.hash_array[hashIndex] = HashTableEntry(key, value)
            self.increment += 1

            # it now has a place
            # update the exisiting key value
            # / create new key value
        else:
            curr_node = self.hash_array[hashIndex]
            while curr_node.key != key and curr_node.next:
                curr_node = curr_node.next
            # if curr_node[key] equals that key ...update the value to match
            if curr_node.key == key:
                curr_node.value = curr_node.value
            # else if its not found, create a (key, value )
            else:
                curr_node.next = HashTableEntry(key, value)
                self.increment += 1
                if self.get_load_factor() > 0.7:
                    # double capacity in size (*2)
                    self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # first item in the hash arr is the head

        # if key == self.head.key:
        #     self.head = self.head.key
        #     return self.head

        prev_head = None
        # curr_head = self.head

        # while curr_head is not None: # loop through until found
        #     if curr_head.key == key:
        #         # if found
        #         prev_head.next = curr_head.next
        #         return curr_head
        #     # move things over -->
        #     prev_head = curr_head
        #     curr_head = prev_head.next
        # return None
        hashIndex = self.hash_index(key)
        curr_node = self.hash_array[hashIndex]

        # if curr_node doesnt exist
        if not curr_node:
            print('does not exist')
        # first item in the hash arr is the head
        elif not curr_node.next:
            self.hash_array[hashIndex] = None
            # take -1
            self.increment -= 1
        else:
            prev_head
        while curr_node.key != key and curr_node.next:
            prev_head = curr_node
            curr_node = curr_node.next
        if not curr_node.next:
            prev_head.next = None
            self.increment -= 1
        else:
            prev_head.next = curr_node.next
            self.increment -= 1
        # When load factor decreases below 0.2,
        #  automatically rehash the table to half its
        # previous size, down to a minimum of 8 slots.
        if self.get_load_factor < 0.2:
            # divide capacity in size = (1/2 capacity)
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # current_node = self.head
        # while current_node is not None:
        #     # if  cur_key = cur_cur_key
        #     if current_node.key == key:
        #         # return cur_key
        #         return current_node
        #     # cur_key = cur_key_next
        #     current_node = current_node.next
        # return None
        hashIndex = self.hash_index(key)
        # if true set current node to that hash_array[index]
        if self.hash_array[hashIndex]:
            curr_node = self.hash_array[hashIndex]
            while curr_node.key is not key and curr_node.next:
                # set curr_node to curr_node.next
                curr_node = curr_node.next
            # if not return the curr_nodes value
            if not curr_node.next:
                return curr_node
            # else return curr_node.value
            else:
                return curr_node.value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # set old hash array to current hash array
        old_hash = self.hash_array

        # create new Hashtable ... capacity = new_capacity
        self.capacity = new_capacity
        self.hash_array = new_capacity * [None]

        # loop  and add each node to latest hashtable (if all are true)
        for node in old_hash:
            if node:
                curr_node = node
                while curr_node is True:
                    self.put(curr_node.key, curr_node.value)
                    curr_node = curr_node.next


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
