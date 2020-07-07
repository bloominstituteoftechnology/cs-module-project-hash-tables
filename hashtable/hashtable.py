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
        self.__storage = [None] * capacity
        self.capacity = capacity
        self.count = 0
        self.should_resize = True

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.__storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return self.count / self.capacity


# algorithm fnv-1 is
#     hash := FNV_offset_basis do

#     for each byte_of_data to be hashed
#         hash := hash × FNV_prime
#         hash := hash XOR byte_of_data

#     return hash 

# All variables, except for byte_of_data, are 64-bit unsigned integers.
# The variable, byte_of_data, is an 8-bit unsigned integer.
# The FNV_offset_basis is the 64-bit FNV offset basis value: 14695981039346656037 (in hex, 0xcbf29ce484222325).
# The FNV_prime is the 64-bit FNV prime value: 1099511628211 (in hex, 0x100000001b3).
# The multiply returns the lower 64-bits of the product.
# The XOR is an 8-bit operation that modifies only the lower 8-bits of the hash value.
# The hash value returned is a 64-bit unsigned integer.

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
        key_bytes = key.encode()

        hash = 5381

        for byte in key_bytes:
            hash = ((hash << 5) + hash) + byte ; # same as hash * 33 + byte
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
        index = self.hash_index(key)

        current_entry = self.__storage[index]

        # Look for existing entry, modify if found
        while current_entry is not None:
            if current_entry.key == key:
                current_entry.value = value
                return

            current_entry = current_entry.next

        # Otherwise, make new entry and link it
        new_entry = HashTableEntry(key, value)
        new_entry.next = self.__storage[index]
        self.__storage[index] = new_entry
        self.count += 1
        self.resize_if_needed()


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        index = self.hash_index(key)

        current_entry = self.__storage[index]

        if current_entry.key == key:
            self.__storage[index] = current_entry.next
            return current_entry

        while current_entry.next is not None:
            if current_entry.next.key == key:
                found_entry = current_entry.next
                current_entry.next = current_entry.next.next
                self.count -= 1
                self.resize_if_needed()
                return found_entry
            
            current_entry = current_entry.next

        print(f"Warning, the key {key} was not found!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        index = self.hash_index(key)

        current_entry = self.__storage[index]

        # Look for key, return value if found
        while current_entry is not None:
            if current_entry.key == key:
                return current_entry.value

            current_entry = current_entry.next
        
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        self.capacity = new_capacity

        old_storage = self.__storage
        self.__storage = [None] * self.capacity

        self.should_resize = False # Pause resizing while re-hashing with new storage

        for slot in old_storage:
            current_entry = slot

            while current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next

        self.should_resize = True

    def resize_if_needed(self):
        if not self.should_resize:
            return

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        elif self.get_load_factor() < 0.2 and self.capacity > MIN_CAPACITY:
            self.resize(self.capacity * 0.5)
        else:
            return

        

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
