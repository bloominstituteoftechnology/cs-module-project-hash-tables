class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        def __repr__(self, key, value):
            return f'{self.key} has {self.value}'


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
        self.table = [None] * self.capacity
        # self.head = None
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
        return len(self.table)

    def get_load_factor(self):
        """   
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        sum = 0
        for index in range(len(self.table)):
            if self.table[index] is not None:
                cur = self.table[index]
                while cur is not None:
                    sum += 1
                    cur = cur.next
        
        load_factor = sum/len(self.table)
        # load_factor = self.count / len(self.table)
        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        FNV_prime = 1099511628211
        FNV_offset = 14695981039346656037
        hashNum = FNV_offset

        # for each byte of data
        for bite in key:
            # hash × FNV_prime
            hashNum = hashNum * FNV_prime
            # hash XOR byte_of_data
            # b = str(bite).encode()
            # hashNum = hashNum ^ b
            hashNum = hashNum ^ ord(bite)

        return hashNum

    # unsigned long
    # hash(unsigned char *str)
    # {
    #     unsigned long hash = 5381;
    #     int c;

    #     while (c = *str++)
    #         hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    #     return hash;
    # }
    # uses xor: hash(i) = hash(i - 1) * 33 ^ str[i], k = 33
     
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hashNum = 5381
        for bite in key:
            hashNum = hashNum * 33 + ord(bite)

        return hashNum

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # value = hashf(s)
	    # return value % len(table)

        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        temp = self.table[index]
        self.table[index] = HashTableEntry(key, value)
        self.table[index].next = temp
            

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # Special case of deleting the head of the list 
           
        pointer = self.table[index]
        if pointer.key == key:
            self.table[index] = pointer.next
            pointer.next = None
            self.count -= 1
            
            return pointer


        # General case
        prev = self.table[index]
        pointer = prev.next
        while pointer is not None:
            if pointer.key == key:
                prev.next = pointer.next
                pointer.next = None
                self.count -= 1
                return pointer
            # pointer is None or # Special case of empty list

        return None

        # def find(self, value):
		# cur = self.head

		# while cur is not None:
		# 	if cur.value == value:
		# 		return cur

		# 	cur = cur.next

		# # If we get here, it's not in the list
		# return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        hash_entry = self.table[index]
        while hash_entry:
            if hash_entry.key == key:
                return hash_entry.value
            else:
                hash_entry = hash_entry.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code 

        load_factor = self.get_load_factor()
        if load_factor < 0.2:
            if self.capacity > 16:
                new_capacity = self.capacity/2 
            else:
                return
        elif load_factor > 0.7:
            new_capacity = 2 * self.capacity
        else:
            return
        if new_capacity < 8:
            return
        old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for i in range(len(old_table)):
            cur = old_table[i]
            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next


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
