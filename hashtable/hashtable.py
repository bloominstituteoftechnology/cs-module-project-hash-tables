class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    # def __repr__(self):
    #     return f"{self.key}, {self.value}"


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
        self.storage = [None] * capacity
        self.total = 0
       


    def get_num_slots(self):
       
        return len(self.storage)


    def get_load_factor(self):
       
        return self.total / self.capacity
        # pass


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_value = 5381
        for c in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(c)
        return hash_value & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
       
      
        # Day 1   
        # new_node = HashTableEntry(key, value)
        # index = self.hash_index(key)
        # if self.storage[index] == None:
        #     self.storage[index] = new_node
        
        # elif self.storage[index].key == key:
        #     self.storage[index].value = value
        index = self.hash_index(key)
        cur_entry = self.storage[index]

        while cur_entry is not None and cur_entry != key:
            cur_entry = cur_entry.next

        if cur_entry is not None:
            cur_entry.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

            self.total += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
  
       


    def delete(self, key):
    
        # Day 1
        # index = self.hash_index(key)
        # if self.storage[index].key == key:
        #     self.storage[index] = None
        index = self.hash_index(key)

        current_entry = self.storage[index]
        last_entry = None

        while current_entry is not None and current_entry.key != key:
            last_entry = current_entry
            current_entry = last_entry.next

        if current_entry is None:
            print("ERROR: Unable to remove entry with key " + key)
        else:
            if last_entry is None: 
                self.storage[index] = current_entry.next
            else:
                last_entry.next = current_entry.next

            self.total -= 1
            if self.get_load_factor() < 0.2:
                if self.capacity > MIN_CAPACITY:
                    new_capacity = self.capacity // 2
                    if new_capacity < MIN_CAPACITY:
                        new_capacity = MIN_CAPACITY

                    self.resize(new_capacity)
        
    def get(self, key):

        # Day 1
        # index = self.hash_index(key)
        # node = self.storage[index]
        
        # if node is not None: 
            
        #     if node.key == key:
        #         return node.value
        index = self.hash_index(key)

        if (self.storage[index] and self.storage[index].key == key):
            return self.storage[index].value
        else:
            return None
    def resize(self, new_capacity):

        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        cur_entry = None
        old_total = self.total

        for total_item in old_storage:
            cur_entry = total_item
            while cur_entry is not None:
                self.put(cur_entry.key, cur_entry.value)
                cur_entry = cur_entry.next

        self.total = old_total

    

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
    print("Should only print 8 lines")
    print("   ")
    print(f"Prints {ht.capacity} lines")
    print("   ")
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
