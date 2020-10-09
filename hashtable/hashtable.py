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

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.hash_array = [None] * capacity
        self.number_of_items = 0
        self.head = None
        self.tail = None
        

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
        return self.number_of_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
         #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis 

        for char in key:
            hash = hash * FNV_prime
            # ord() returns an integer representing the Unicode character
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000

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
        self.number_of_items += 1
        index = self.hash_index(key)
        node = self.hash_array[index]

        if node is None:
            self.hash_array[index] = HashTableEntry(key, value)
            self.number_of_items += 1
            return
        
        while node.next != None and node.key != key:
            node = node.next
        
        if node.key == key:
            node.value = value
        else:
            node.next = HashTableEntry(key, value)
            self.number_of_items += 1


        # if hash_array is None:
        #     self.hash_array[index] = HashTableEntry(key, value)
        #     return
        # prev = None

        # while node is not None:
        #     prev = node
        #     node = node.next
        # prev.next = HashTableEntry(key, value)



      

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.hash_array[index]
        prev = None

        if node is not None:
            while node.next != None and node.key != key:
                prev = node
                node = node.next
            if node.key == key:
                if prev is None:
                    self.hash_array[index] = node.next
                else:
                    prev.next = node.next
                self.number_of_items -= 1
                return
        
        # while node is not None and node.key != key:
        #     prev = node
        #     node = node.next
        # if node is None:
        #     return None
        # else:
        #     self.number_of_items -= 1
        #     result = node.value
        #     if prev is None:
        #         node = None
        #     else:
        #         prev.next = prev.next.next
        #         return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.hash_array[index]

        if node is None:
            return None
        while node.next != None and node.key != key:
            node = node.next
        return node.value if node.key == key else None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # new_hash_array = [None] * new_capacity
        # old_hash_array = self.hash_array

        # self.hash_array = new_hash_array
        # self.count = 0
        # self.capacity = new_capacity

        # current_index = 0
        # while current_index < len(old_hash_array):
        #     current_node = old_hash_array[current_index]
        #     if current_node is not None:
        #         next_node = current_node.next
        #         current_node.next = None
        #         self.put(current_node.key, current_node.value)
        #         old_hash_array[current_index] = next_node
        #     elif current_node is None:
        #         current_index += 1 
        # return

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
