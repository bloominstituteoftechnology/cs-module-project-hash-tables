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
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.storage= [None] *  capacity      

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


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # FNV_offset_basis = 14695981039346656037 
        # FNV_prime = 1099511628211
        # key_bytes = key.encode()
        # Your code here
        # hashed_result = FNV_offset_basis
        
        # key_bytes = key.encode()
        
        # for byte in key_bytes:
        #     hashed_result = hashed_result + FNV_prime
            
            
            ##wheres the symbol?
            # hashed_result = hashed_result byte
            # hashed_result = hashed_result ^ byte

            
        # return hashed_result   
        str_bytes = str(key).encode()
        total = 0
        for b in str_bytes:
            total +=b
            total &= 0xFFFFFFFFFFFFFFFF
        return total

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash = 5381
         
        # for char in key:
        #     hash = (hash*33)* ord (char)
        # return hash
        
        str_bytes = str(key).encode()
        total = 0
        for b in str_bytes:
            total+=b
            
            total &= 0xFFFFFFFF
        return total    
        
        # hashed_result = 5381
        
        # key_bytes = key.encode()
        
        # for b in key_bytes:
        #     hashed_result= ((hashed_result <<5)+hashed_result)+b
            
        # return hashed_result    
    
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
        idx = self.hash_index(key)
         
         
         
        if self.storage[idx] != None:
             #check if the key is already in our linked list
             node = self.storage[idx] #this is the head
             
             while node is not None:
                 if node.key == key:
        
             ##If so, overwrite that value
                    node.value = value
                    return
            ## if not add a node to the head of the linked list
                    old_head = self.storage[idx] 
                    new_head = HashTableEntry(key,value)
                    new_head.next = old_head
                    self.storage[idx]=new_head
        else:    
            self.storage[idx]  = new_head
            
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_key = self.hash_index(key)

        node = self.storage[hashed_key]

        if node.key == key:
            self.storage[hashed_key] = node.next
            return

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f"{key} was not found")
            return None
        prev.next = node.next
        
  ## Teachers code
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key) 
        node = self.storage[idx]
        # return value 
        while node is not None:
            if node.key == key:
                node = node.value
            node = node.next
        return None         
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = self.capacity *2
        new_storage = [None] * self.capacity
        
        for i in range(len(self.storage)):
            node = self.storage[i]
            
            while node is not None:
                hashed_key = self.hash_index(node.key)
                new_storage[hashed_key]=node
                node = node.next
        self.storage = new_storage        

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
