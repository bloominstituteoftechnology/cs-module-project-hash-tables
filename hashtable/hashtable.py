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
        self.storage = [None] * capacity
        self.head = None
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()
        
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

        Implement this.

        O(n) over the length (number of bytes) of the key
	    O(1) over the number of items in the table
        """
        # Your code here
        # get index of key
        index = self.hash_index(key)
        self.head = self.storage[index]

        # search the linked list at the index for the key
        while self.head:
            # if the key is found, overwrite the value stored there
            if self.head.key == key:
                self.head.value = value
            self.head = self.head.next
        # else insert the key and value at the head of the list at that index
        newNode = HashTableEntry(key, value)
        newNode.next = self.storage[index]
        self.storage[index] = newNode
        self.size += 1

        # If load factor goes beyond threshold, then 
        # double hash table size 
        if self.get_load_factor() >= 0.7:
            self.resize(self.get_num_slots() * 2)

        # if self.get_load_factor() <= 0.2:
        #     self.resize(self.get_num_slots() / 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index for the key
        index = self.hash_index(key)
        self.head = self.storage[index]

        # search the linked list for the key at that index
        while self.head:
            # if found, delete it, return it
            if self.head.key == key:
                old_head = self.head
                self.storage[index] = self.head.next
                old_head.next = None
                self.size -= 1
                return old_head

        # else return None
        print(f'{key} is not found in the hash table')
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.head = self.storage[index]
    
        # search the linked list at that index for the key
        while self.head:
            # if found, return the value
            if self.head.key == key:
                return self.head.value
            self.head = self.head.next

        # else return None
        return None

# ignore - for tomorrow
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # Make a new array 2x the size of the old one
        oldStorage = self.storage
        self.storage = [None] * new_capacity
        #set capacity to new size
        self.capacity = new_capacity
        #reset the items count
        self.items = 0

	    # for each entry in the list at that index:
        for entry in oldStorage:
            while entry is not None:
                # Add it to the new array
                self.put(entry.key, entry.value)
                entry = entry.next



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
