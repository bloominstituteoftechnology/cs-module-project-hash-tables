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
MAX_LOAD_FACTOR = .7


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.array = [None] * capacity #where the list starts[None] so thing can be added
        self.number_of_items = 0
        self.head = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.number_of_items / self.get_num_slots()

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
        # Your code here
        long_hash = 5381

        for hashs in key:
            long_hash= long_hash * 33 * ord(hashs)

        return long_hash




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
        index = self.hash_index(key)
        self.head = self.array[index]
        while self.head: # searching the linked list
            if self.head.key == key:
                #if the key is found put the value there
                self.head.value = value
            self.head = self.head.next
            #put the key, value at the head
        new_node = HashTableEntry(key,value)
        new_node.next = self.array[index]
        self.array[index] = new_node
        self.number_of_items += 1

        if self.get_load_factor() >= .7:
               #if its bigger then.07 double the size
            self.resize(self.get_num_slots()*2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # Your code here
        index = self.hash_index(key)
        self.head = self.array[index]

        while self.head:# searching ll
            if self.head.key == key: #deleting
                prev_head = self.head
                self.array[index]= self.head.next
                prev_head.next = None
                self.number_of_items -+ 1
                return prev_head

        print(f'{key} is not not found.')
        return None



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.head = self.array[index]
        while self.head:#search LL
            if self.head.key ==key: #if found return value
                return self.head.value
            self.head = self.head.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #create a blank array, with a double size of old array
        #we have to rehash every single item because the hash function has changed
            #go through each slot in the array
            #go through each iten in each linked list in the array
            #rehash the key in each item and store it in new array

        #make new array the new storage O(n)
        old_array = self.array #make new array
        self.array = [None] * new_capacity
        self.capacity = new_capacity#new size
        self.items = 0 #reset items

        for array in old_array:
            while array is not None:
                #added it to new list
                self.put(array.key, array.value)
                array = array.next




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

    #Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
