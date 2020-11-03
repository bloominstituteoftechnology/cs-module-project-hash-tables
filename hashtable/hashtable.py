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
          # Your code here
        # initialize the hash table with empty storage list entries
        # size of the array = min 8
        # will store our data in - set equal to None force python to get a list that has a fixed length
        self.capacity = MIN_CAPACITY
        self.bucket = [None] * self.capacity
        self.count = 0

    def __repr__(self):
        return str(self.capacity)

    def get_num_slots(self):
        # Your code here
        return len(self.bucket)


    def get_load_factor(self):
        # Your code here
        return self.count / len(self.bucket)


    def fnv1(self, key):
        pass
       

    def djb2(self, key):
        hash = 5381
        # iterates characters in key,
        for character in key:
            # ord: numerical value of that character -->
            hash = ((hash << 5) + hash) + ord(character)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        idx = self.hash_index(key)
        
        node = HashTableEntry(key,value)
        
        key = self.bucket[idx]
        
        self.count += 1

        # the key exist
        if key:
            # overwrite with the node
            self.bucket[idx] = node
            self.bucket[idx].next = key
        # if self.capacity[index] exist,
        # use LL to set next to the repeated key and value
        else:
            self.bucket[idx] = node
        # print('adding node', node.next)
        print(self.bucket)
        return self.bucket[idx]

    def delete(self, key):
        self.count -= 1
        self.put(key, None)
       
    def get(self, key):
        idx = self.hash_index(key)
        
        arr = self.bucket[idx]
        
        while arr:
            if arr.key == key:
                return arr.value
            arr = arr.next
       


    def resize(self, new_capacity):
        
        if self.get_load_factor() < 0.2:
            self.capacity = new_capacity // 2                           
            prev_bucket = self.bucket             # [None, None, None, None, None, None, None, None].
            self.bucket = [None] * self.capacity  # [None, None, None, None]
             
            for node in prev_bucket:    # Traverse thru all the nodes. 
                               
                if node != None:
                    self.put( node.key, node.value )
                else:
                    continue
        
        
        if self.get_load_factor() > 0.7:
            self.capacity = new_capacity * 2                           
            prev_bucket = self.bucket            # [None, None, None, None, None, None, None, None].
            self.bucket = [None] * self.capacity
            
            for node in prev_bucket:    # Traverse thru all the nodes. 
                               
                if node != None:
                    self.put( node.key, node.value )
                else:
                    continue
                
                        
        
        
        
        
        



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
