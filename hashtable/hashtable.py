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
        self.array = [None] * capacity
        self.node_count = 0
        if capacity < MIN_CAPACITY:
            self.capacity  = MIN_CAPACITY
        else:
            self.capacity = capacity



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return(len(self.array))


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return(self.node_count/len(self.capacity))


    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """

    #     hash_key = 14695981039346656037
    #     fnv_prime = 1099511628211  
    #     word = str(key)
    #     key_bytes = word.encode()

    #     for byte in key_bytes:
    #         hash_key = (hash_key * fnv_prime) ^ byte
        
    #     return hash_key


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        word = str(key)
        key_bytes = word.encode()

        for byte in key_bytes:
            hash = (hash * 33 + hash + byte)

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

        if self.array[index] is None:
            self.array[index] = new_node
            self.node_count += 1
        else:
            node = self.array[index]
            while node.next is not None:
                if node.key == key:
                    node.value = value
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = new_node
                self.node_count += 1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)

        if self.array[index] is None:
            return None
        elif self.array[index].next is None:
            self.array[index] = None
            self.node_count -= 1
        else:
            node =self.array[index]
            prev_node = None
            while node.key is not key:
                prev_node = node
                node = node.next
            if node.next is None:
                node = None
                prev_node.next = None
                self.node_count -= 1
            elif prev_node is None:
                self.array[index] = node.next
                self.node_count -= 1
            else:
                prev_node.next = node.next
                node = None
                self.node_count -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.array[index] is None:
            return None
        elif self.array[index].next is None:
            if self.array[index].key == key:
                return self.array[index].value
            else:
                return None
        else:
            node = self.array[index]
            while node.key != key:
                if node.next is None:
                    return None
                node = node.next
            return node.value
            

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        previous_array = self.array
        new_array = [None] * new_capacity
        self.array = new_array
        self.capacity = new_capacity
        self.number_of_items = 0
        for hash_Node in previous_array:
            while hash_Node != None:
                self.put(hash_Node.key, hash_Node.value)
                hash_Node = hash_Node.next    


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
