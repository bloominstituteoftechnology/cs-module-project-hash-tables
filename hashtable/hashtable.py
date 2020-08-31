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

    def __init__(self, capacity):
        self.capacity = capacity;
        self.size = 0;
        self.slots = [None]*self.capacity;

    def get_num_slots(self): return len(self.slots)
    def get_load_factor(self): return self.size / self.len(self.slots)

    def fnv1(self, key):
        # FNV-1 Hash, 64-bit
        hsh = 14695981039346656037; # 64bit ( &= 0xcbf29ce484222325 ) or ( 14695981039346656037 )
        fnv_prime = 1099511628211; # 64bit (240 + 28 + 0xb3) or ( 1099511628211 )

        for char in key:
            hsh = hsh * fnv_prime 
            hsh = hsh ^ ord(char)

        return hsh

    def djb2(self, key):
        # DJB2 hash, 32-bit
        hsh = 5381

        for char in key:
            hsh = (( hsh << 5) + hsh) + ord(char)

        print(f' hashing key: {key} to {hsh & 0xFFFFFFFF % self.capacity}')
        return hsh & 0xFFFFFFFF


    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index
        # between within the storage capacity of the hash table.

        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Hash collisions should be handled with Linked List Chaining.
        """
        # Your code here
        self.size += 1 # increment size
        self.slots[self.hash_index(key)] = value; # Store the value with the given key.
        print(f'value = {value} and key = {key}')
        print(self.hash_index(key)) 


    def delete(self, key):
        if self.slots[self.hash_index(key)] is None: # Checking if the variable is None
            print("Invalid key input.");
        else:
            self.size -= 1; # decrement size
            self.slots[self.hash_index(key)] = None; # Remove the value stored with the given key.

    def get(self, key):
        if self.slots[self.hash_index(key)] is None: # Checking if the variable is None
            print("Invalid key input.");
            return None # Returns None if the key is not found.
        else:
            print(f'returning key: {key} as {self.slots[self.hash_index(key)]}')
            return self.slots[self.hash_index(key)] # Return the value stored with the given key.

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
