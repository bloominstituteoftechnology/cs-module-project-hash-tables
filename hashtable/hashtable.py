'''
    Great articles 
        First one explains what a hash table is 
        
        https://www.educative.io/edpresso/what-is-a-hash-table
        
        second one explains what a hash table collision and chaining is 
        
        https://www.educative.io/edpresso/what-is-chaining-in-hash-tables
        
'''

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
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        self.storage = [None]*self.capacity
        self.item_stored = 0
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        print('Capacity of this hashtable: ', self.capacity)
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.item_stored/self.capacity
        


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
        hash_index = self.hash_index(key)
        # self.data[index] = value
        
        #insert into an emtpy spot 
        if not self.storage[hash_index]:
            self.storage[hash_index] = HashTableEntry(key, value)
            self.item_stored += 1
            
        #linked list exist current location
        #update the value of the existing key
        #or we can create a new entry for the new key 
        else: 
            current = self.storage[hash_index]
            
            while current.key != key and current.next:
                current = current.next

            #find key and update the current value
            if current.key == key:
                current.value = value
                
            #key is not found then add an entry 
            else:
                current.next = HashTableEntry(key, value)
                self.item_stored += 1
            # resize if load factor is too big
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity*2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]
        #if nothing to delete
        if not current:
            print("The key is not found")
        
        #1 element, the head in the index bucket
        elif not current.next:
            self.storage[hash_index] = None
            self.item_stored -= 1
        #store a pointer to the previous node
        else:
            prev = None
            
            #move to next node 
            #if key won't match and there is a next
            while current.key != key and current.next:
                prev = current
                current = current.next
            
            #value to delete int he edn of index
            if not current.next:
                prev.next = None
                self.item_stored -= 1
            #value in the middle of index bucket
            else:
                prev.next = current.next
                self.item_stored -= 1
            
            #if loader factor is too small resize it 
            if self.get_load_factor() < 0.2:
                self.resize(self.capacity // 2)
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.storage[hash_index]:
            current = self.storage[hash_index]
            while current.key is not key and current.next:
                current = current.next
            if not current.next:
                return current.value
            else:
                return current.value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        old_storage = self.storage

        # initialize new hashtable
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # loop through and add each node to new hashtable
        for item in old_storage:
            if item:
                current = item
                while current:
                    self.put(current.key, current.value)
                    current = current.next




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