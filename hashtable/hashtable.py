class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current_str = ""
        current = self.head
        while current is not None:
            current_str += f"{str(current.value)} -> "
            current = current.next
        return current_str

    def add_to_head(self, node):
        node.next = self.head
        self.head = node

    def add_to_head_or_overwrite(self, node):
        existing_node = self.find(node.key)
        if existing_node is not None:
            existing_node.key = node.key
        else:
            self.add_to_head(node)

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head

        if current.key == key:
            self.head = current.next

        prev = current
        current = current.next

        while current is not None:
            if current.key == key:
                prev.next = current.next
                current.next = None
                return current.value
            else:
                prev = current
                current = current.next

        return None


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
        self.table = [None] * capacity

        for i in range(0, len(self.table)):
            self.table[i] = LinkedList()


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        
         One of the tests relies on this. if froggy do tonight 🤣
        
        Implement this.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        count = 0

        for i in range(0, len(self.table)):
            current = self.table[i].head
            while current is not None:
                count += 1
                current = current.next
        
        load_factor = count / self.get_num_slots()
        
        if load_factor > 0.7:
            self.resize(self.capacity * 2)
        elif load_factor < 0.2:
            if self.capacity // 2 < 8:
                self.resize(8)
            else:
                self.resize(self.capacity // 2)
        
        return load_factor


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
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
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
        new_entry = HashTableEntry(key, value)
        self.table[self.hash_index(key)].add_to_head(new_entry)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        return self.table[self.hash_index(key)].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        if self.table[self.hash_index(key)].head is not None:
            return self.table[self.hash_index(key)].find(key)
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        old_capacity = self.capacity
        self.capacity = new_capacity

        for i in range(old_capacity, new_capacity):
            self.table.append(None)
            self.table[i] = LinkedList()

        for i in range(0, old_capacity):
            current_node = self.table[i].head
            while current_node is not None:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next        


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

    # # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")