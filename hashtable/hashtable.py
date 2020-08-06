class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __repr__(self):
        return repr(self.key)



class LL:
    def __init__(self):
        self.head = None

    # this basically goes through the list until the matching key is found
    # if no matching key is found it returns None
    def find_current_node(self,key):
        curr = self.head

        while curr is not None:
            
            if curr.key == key:
                
                return curr
            
            curr = curr.next
            
        return None

    def add_to_head(self,key,value):
        node = HashTableEntry(key,value)
        # this switches the pointers around so that the current head can switch
        if self.head is not None:
            node.next = self.head

        self.head = node

    def delete(self,key):
        curr = self.head
        # if the node is already None theres no reason to change anything
        if curr is None:
            return None
        # if the key matches for head we can modify pointers for deletion
        if curr.key == key:
            self.head = curr.next
            return curr
        # this is for deleting non head nodes
        else:
            prev = curr
            curr = curr.next

            while curr is not None:
                if curr.key == key:
                    # this turns pointers away from current for deletion
                    prev.next = curr.next
                    return curr 
            return None

        


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.count = 0

        for x in range(self.capacity):
            self.hash_table[x] = LL()
        


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


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hashed = 5381
        for c in key:
            hashed = (hashed * 33) + ord(c)
        return hashed       


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
        load_factor = self.get_load_factor()

        # this doubles the hash map if the number of occupied space exceeds 70%
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

        index = self.hash_index(key)
            # this is to check for existing nodes to avoid clash

        search_node = self.hash_table[index].find_current_node(key)
        # if the head is not empty we set it to the current value to place
        if search_node is not None:
            search_node.value = value
            
        # otherwise we set the head and increase count
        else:
            self.hash_table[index].add_to_head(key,value)
            #print("TABLE: \n",self.hash_table)
            self.count+=1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        deleted = self.hash_table[index].delete(key)

        if deleted is None:
            print('Key {} not found!'.format(key))
        else:
            print('Key {} deleted'.format(key))
            self.count -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        
        # we check for the key using the hash index 
        LL_res = self.hash_table[index].find_current_node(key)
        # we check if the key can be found. if not it returns None
        # if it is found it returns the matching value
        if LL_res is None:
            return None
        return LL_res.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # need to save old values
        old_hash_table = self.hash_table

        # make a new table for resized list
        new_hash_table = [None] * new_capacity

        self.count = 0

        for x in range(new_capacity):
            new_hash_table[x] = LL()
##            print("X_NEW_CAP \n",x)
##            print("NEW_TBL: \n",new_hash_table)

        self.hash_table = new_hash_table

        self.capacity = new_capacity

        self.count = 0
        # iterate through the old hash table
        for y in old_hash_table:
            curr = y.head
            
            # this keeps going until the next node is None. which means that
            # there are no more nodes to add
            while curr is not None:
                # this finally stores the new array
                self.put(curr.key,curr.value)

                curr = curr.next

    def __str__(self):

        return "".join(str(item) for item in self.hash_table)



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

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
