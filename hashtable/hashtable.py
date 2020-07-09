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
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.capacity = capacity
        self.usage = 0
        self.list = [[None] for i in range(capacity)]
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.capacity)


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

        key_to_strBytes = str(key).encode()
        hash_value = 5381
        for i in key_to_strBytes:
            hash_value = ((hash_value << 5) + hash_value) + i
            hash_value &= 0xffffffff
        return hash_value


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash_value = 5381
        for i in key:
            hash_value = (hash_value * 33) + ord(i)
        return hash_value


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
        self.count += 1
        load = self.get_load_factor()

        if load > 0.9:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
        hashTable = HashTableEntry(key,value)
        if self.list[index] is None:
            current = self.list[index]
            prev = current #head
            while current is not None:
                if cur.key == key:
                    prev.next = hashTable
                    self.delete(key)
                    return
                else:
                    prev = current
                    current = current.next
            prev.next = hashTable
            
        else:
            self.list[index] = hashTable


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.list[index] is not None:
            current = self.list[index]
            if current.key == key:
                if cur.next is not None:
                    current = current.next
                    self.list[index] = current
                else:
                    self.list[index] = None
                return current

            prev = current
            current = current.next

            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    current.next = None
                    return current
                else:
                    prev = prev.next
                    current = current.next
            return None
        else:
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.list[index] is not None:
            current = self.list[index]
            while current is not None:
                if current.key == key:
                    return current.value
                current = current.next
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        index = 0
        new_list = [[None] for i in range(new_capacity)]
        for i in self.list:
            new_list[index] = i
            index += 1
        self.list = new_list




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
