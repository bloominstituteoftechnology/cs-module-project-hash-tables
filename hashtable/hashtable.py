class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    #  def __repr__(self):
    #     contents = ''
    #     current_node = self

    #     while current_node.next:
    #         contents += str(self.value) + ' => '
    #         current_node = current_node.next

    #     contents += 'None'

    #     return contents


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
        self.items_stored = 0
        self.storage = [None] * capacity

    def __repr__(self):
        report = f"Hashtable\n {self.items_stored}/{self.capacity} items stored.\n"
        contents = "\n".join([str(index) + ": " + str(linked_list) for index, linked_list in enumerate(self.storage)])

        return report + contents


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


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
        # Your code here
        key_bytes = key.encode()
        hash = 5381
        for k_byte in key_bytes:
            hash = hash * 33 + k_byte
            hash &= 0xffffffff
            
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
        # Your code here

        # i = self.hash_index(key)
        # self.storage[i] = value

        hash_index = self.hash_index(key)

        if not self.storage[hash_index]:
            self.storage[hash_index] = HashTableEntry(key, value)
            self.items_stored += 1

        else:
            current_node = self.storage[hash_index]

            while current_node.key != key and current_node.next:
                current_node = current_node.next

            if current_node.key == key:
                current_node.value = value

            else:
                current_node.next = HashTableEntry(key, value)
                self.items_stored += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # i = self.hash_index(key)
        # self.storage[i] = None

        index = self.hash_index(key)

        current_node = self.storage[index]

        if not current_node:
            return 'none'

        elif not current_node.next:
            self.storage[index] = None
            self.items_stored -= 1

        else:
            previous_node = None

            while current_node.key != key and current_node.next:
                previous_node = current_node
                current_node = current_node.next

            if not current_node.next:
                previous_node.next = None
                self.items_stored -= 1

            else:
                previous_node.next = current_node.next
                self.items_stored -= 1

        if self.get_load_factor() < 0.2:

            new_capacity = self.capacity // 2

            if  new_capacity < MIN_CAPACITY:
                new_capacity = MIN_CAPACITY

            self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        
        # i = self.hash_index(key)
        # return self.storage[i]

        index = self.hash_index(key)

        if self.storage[index]:
            current_node = self.storage[index]

            while current_node.key != key and current_node.next:
                current_node = current_node.next

            if not current_node.next:
                return current_node.value

            else:
                return current_node.value

        else:
            return None

                

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
