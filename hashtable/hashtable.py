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
        self.hash_array = [None]*capacity
        self.capacity = capacity
        self.number_of_items = 0
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.hash_array)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        load_factor = self.number_of_items/self.get_load_factor()
        return load_factor


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
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
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
        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        # if there is an item at the given index, but need to be overwritten
        current = self.hash_array[index]
        while current is not None:
            if current.key == key:
                #over the current value with the given value
                current.value = value
            current = current.next    

        # if there are no items present at the given index
        if self.hash_array[index] == None:
            self.hash_array[index] = new_entry
        # if there is at least one item at the given index    
        else:
            new_entry.next = self.hash_array[index]
            self.hash_array[index] =   new_entry

        self.number_of_items += 1    



    def delete(self, key):
        """ Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this."""
        # Your code here
        index = self.hash_index(key)
        if index > self.capacity:
            print("Out of range!!!")
        if self.hash_array[index] == None:
            print('Key not found') 

        previous = None
        current = self.hash_array[index]    
        if key == current.key:
            self.hash_array[index] = current.next
            return current.value  
        while current != None:
            #keep looping until we find the correct key
            if current.key == key:
                previous.next = current.next
                return current.value
            previous = current
            current = current.next 
        self.number_of_items -= 1    
        return None      

        print(f"the current head is {current.value}") 
 




    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        index_value = self.hash_index(key)
        current = self.hash_array[index_value]
        while current != None:
            if current.key == key:
                return current.value
            current = current.next        
    
        return None  


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        previous_array = self.hash_array
        new_array = [None] * new_capacity
        self.hash_array = new_array
        self.capacity = new_capacity
        self.number_of_items = 0
        for hashNode in previous_array:
            while hashNode != None:
                self.put(hashNode.key, hashNode.value)
                hashNode = hashNode.next        




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
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

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
