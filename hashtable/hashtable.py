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
        self.bucket = [None] * capacity
        self.capacity = capacity
        self.count = 0


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
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211 

        hashed_var = FNV_offset_basis

        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b

        return hashed_var


    # def djb2(self, key):
    #     """
    #     DJB2 hash, 32-bit

    #     Implement this, and/or FNV-1.
    #     """
    #     hash = 5381
    #     byte_array = key.encode('utf-8')
        
    #     for byte in byte_array:
    #         hash = ((hash * 33) ^ byte) % 0x100000000
            
    #     return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Cast the key to a string and get bytes
        #str_key = str(key).encode()
        # Start from an arbitrary large prime
        hash = 5381
        # Bit-shift and sum value for each character
        for b in key:
            hash = (hash * 33) + ord(b)
            #hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits
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

        item = HashTableEntry(key, value)
        index = self.hash_index(key)
        # # self.bucket.insert(self.hash_index(key), HashTableEntry(key, value))
        # self.bucket[index] = item
        cur = self.bucket[index]

        # while cur != None and cur.key != key:
        #     cur = cur.next
        # if cur != None:
        #     cur.value = value
        # else:
        #     item.next = self.bucket[index]
        #     self.bucket[index] = item
        #     self.count += 1

        if cur:
            last_entry = None
            while cur:
                if cur.key == key:
                    # found existing key, replace value
                    cur.value = value
                    return
                last_entry = cur
                cur = cur.next # for the next run # if next == None ends while loop 
            # if we get this far, we didn't find an existing key
            # so just append the new node to the end of the bucket
            last_entry.next = item
            self.count += 1
        else:
            self.bucket[index] = item
            self.count += 1

        if self.get_load_factor() >= 0.7: # max 1 for test
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        # self.bucket.pop(index)
        cur = self.bucket[index]

        if cur:
            last_entry = None
            while cur:
                if cur.key == key:
                    if last_entry:
                        last_entry.next = cur.next
                    else:
                        self.bucket[index] = cur.next
                    self.count -= 1
                last_entry = cur
                cur = cur.next

        if self.get_load_factor() <= 0.2:
            self.resize(self.capacity * 0.5)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        index = self.hash_index(key)
        
        # if self.bucket[index]:
        #     value = self.bucket[index].value
        #     return value
        # else:
        #     return None

        cur = self.bucket[index]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        old_bucket = self.bucket
        self.bucket = [None] * new_capacity
        self.capacity = new_capacity
        for x in old_bucket:
            if x:
                self.put(x.key, x.value)
        
        

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
