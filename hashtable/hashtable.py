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
        self.load = 0
        self.table = [None] * self.capacity

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
        # dont do yet
        # number of items divided by number of buckets
        # try to keep between 20% and 70%
        return self.load / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        # what is a FNV-1 Hash, 64 bit?
        # Non-crytographic hash function created by Glenn Fowler, London Curt Noll, and Kiem-Phong Vo.
        # Constatnts
        # Start with an initail hash value
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        key_of_data_bytes = key.encode()

        hash = offset_basis
        for letter in key_of_data_bytes:
            hash = hash * FNV_prime
            # Use the XOR operator ^ between two values to perform bitwise "exclusive or" on their binary representations. When used between two integers, the XOR operator returns an integer.
            hash = hash ^ letter

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
        """
        # Your code here
        # hashed_string = self.hash_index(key)

        # if self.table[hashed_string] != None:
        #     print("warning collistion!!!")

        # self.table[hashed_string] = value

        # self.load += 1
        hashed_string = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        curr = self.table[hashed_string]

        if self.table is not None:
            self.table[hashed_string] = new_node
            self.table[hashed_string].next = curr
        else:
            self.table = new_node
        self.load += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # hashed_string = self.hash_index(key)
        # if self.table == None:
        #     print("warning no key!!")

        # else:

        #    self.table[hashed_string] = None

        #    self.load -= 1
        hashed_string = self.hash_index(key)
        removed = False

        if self.table[hashed_string].key == key:
            self.table[hashed_string] = self.table[hashed_string].next
            self.load -= 1
            removed = True

        else:
            curr = self.table[hashed_string]
            prev_node = None

            while curr is not None:
                if curr.key == key:
                    prev_node.next = curr.next
                    self.load -= 1
                    removed = True

                    return

                prev_node = curr
                curr = curr.next
            if removed == False:
                print("warning no key!!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # hashed_string = self.hash_index(key)

        # value = self.table[hashed_string]

        # return value if value else None
        hashed_string = self.hash_index(key)
        current_node = self.table[hashed_string]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # save your old storage in a new variable
        # make a new storage , with new capacity
        # then loop over your old starage
        #  for each index, if its not not
        # iterate through the linked list
        # for each node , call put for key and value
        # that way, its rehashed and inserted to new storage
        # self.load remain the same
        # self.capacity
        #
        new_hashtable = HashTable(new_capacity)

        for i in range(self.capacity):
            if self.table[i] is not None:
                entry = self.table[i]
                while entry:
                    new_hashtable.put(entry.key, entry.value)
                    entry = entry.next

        self.table = new_hashtable.table
        self.capacity = new_capacity
        self.load = new_hashtable.load


hash_table = HashTable(100)

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
