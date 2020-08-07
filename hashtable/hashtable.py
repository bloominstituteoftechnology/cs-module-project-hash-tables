# Import libraries, packages, modules needed:
import sys


class HashTableEntry:
    """
    Linked List node with hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find(self, key):
        pass

    def insert(self, key, value):
        pass

    def delete(self, key):
        pass


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` number of buckets
    that accepts string keys.

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None for number in range(self.capacity)]


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


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
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        
        # Apply FNV-1 hash function to bytes representations:
        fnv_offset_basis = 14695981039346656037  # Same in hexadecimal: 0xcbf29ce484222325
        fnv_prime = 1099511628211  # = 2**40 + 2**8 + 0xb3, or in hex: 0x100000001b3
        hash_code = fnv_offset_basis
        for byte in key_as_bytes:
            # Faster C-style alt. syntax for the below: hash = ((hash << 5) + hash) + char
            hash_code *= fnv_prime
            hash_code = hash_code ^ byte
        
        # Modulo the result to make sure it is an index within the existing array:
        hash_code %= self.capacity
        
        return hash_code


    def djb2(self, key):
        """
        DJB2 hash function, 32-bit
        """
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        # Apply DJB2 hash function to bytes representations:
        hash = 5381
        for byte in key_as_bytes:
            # Faster C-style alt. syntax for the below: hash = ((hash << 5) + hash) + char
            hash = hash * 33 + byte
        
        # Modulo the result to make sure it is an index within the existing array:
        hash %= self.capacity
        
        return hash


    def djb2_xor(self, key):
        """
        DJB2 hash function, 32-bit
        """
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        # Apply DJB2 hash function to bytes representations:
        hash = 5381
        for byte in key_as_bytes:
            # The ^ operator below is the bitwise XOR operator:
            hash = ((hash * 33) ^ byte)  # Q: Should we then % 128 (same as % 0x10000000) this to "keep it 32-bit" bc "python ints don't overflow"?
        
        # Modulo the result to make sure it is an index within the existing array:
        hash %= self.capacity
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key)
        return self.djb2(key)


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Get index for this key from our hash function:
        index = self.djb2(key)
        # Put the value for this key at that index:
        self.array[index] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Get index for this key from our hash function:
        index = self.djb2(key)
        # "Delete" the value at that index (for the provided key) by setting it back to None:
        self.array[index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get index for this key from our hash function:
        index = self.djb2(key)
        # Return the value at that index (the value corresponding to the provided key):
        return self.array[index]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
