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

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        self.list = [LinkedList()] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        # IMPLEMENT
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        # Default prime and offset values
        FNV_PRIME = 1099511628211
        FNV_OFFSET_BASIS = 14695981039346656037
        hash = FNV_OFFSET_BASIS

        # For each char, mutliply by FNV_PRIME to get a 64 bit number then modify the lower 8 bits of the char
        for char in key:
            hash = hash * FNV_PRIME
            hash = hash ^ ord(char)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """
        # Prime number, divides well
        hash = 5381

        # For each char, multiply the hash by 33 and add the unicode integer of the char
        for char in key:
            hash = (hash * 33) + ord(char)
        
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        # Naive Approach
        # hash = self.hash_index(key)

        # if hash <= self.capacity:
        #     self.list[hash] = value

        # Chaining Approach
        hash = self.hash_index(key)
        hash_entry = HashTableEntry(key, value)

        if self.list[hash].head is None:
            self.list[hash].head = hash_entry
        else:
            current = self.list[hash].head
            while current.next:
                if current.key == key:
                    current.value = value
                current = current.next
            
            current.next = hash_entry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        # Naive Approach
        # hash = self.hash_index(key)

        # if hash <= self.capacity:
        #     self.list[hash] = None
        # else:
        #     print('Key not found')

        # Chaining Approach
        hash = self.hash_index(key)
        current = self.list[hash].head
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                    return
                else:
                    self.list[hash].head = self.list[hash].head.next
                    return
            
            previous = current
            current = current.next
        
        print('Key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        # Naive Approach
        # hash = self.hash_index(key)

        # if hash <= self.capacity:
        #     return self.list[hash]
        # else:
        #     return None

        # Chaining Approach
        hash = self.hash_index(key)
        current = self.list[hash].head

        if current is None:
            return None
        
        if current.key == key:
            return current.value

        while current.next:
            current = current.next

            if current.key == key:
                return current.value
        
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # IMPLEMENT
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

    print("")