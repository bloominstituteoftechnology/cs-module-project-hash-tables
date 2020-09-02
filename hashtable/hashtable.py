class HashTableEntry:
    """
    Linked List hash table key/value pair

    """
    # Each of the entries will be in the linked list
    # if there is a collision then we will build the linked list 
    # and and the value further down
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

    def __init__(self, capacity=16): 
        # Your code here
        self.myList =  [None] * capacity# this is the length of the list
                                 # default initail capacity is at 16
        self.capacity = capacity
        self.num_vals_entered = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_vals_entered / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # check if the key is a string
        # if isn't a string will make it a string
        if not isinstance(key, str):
            key = str(key)

        FNV_offset = 14695981039346656037
        FNV_prime = 0x100000001b3

        theHash = FNV_offset
        # encoding the string
        encoded = key.encode()
        # loop through the bytes of the encoded
        for b in encoded:
            theHash = theHash * FNV_prime
            theHash = theHash ^ b
        theHash &= 0xffffffffffffffff
        return theHash


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
        
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # will check to see if we want to resize
        if self.get_load_factor() > .7:
            self.resize(self.capacity*2)
        # want to first get the index first
        theIndex = self.hash_index(key)
        # Go to the index and see if there is anything in the 
        # index
        if self.myList[theIndex] == None:

            self.myList[theIndex] = HashTableEntry(key, value)

            self.num_vals_entered += 1 # doing the incrementing here if there is nothing
                  
        else:
            self.input_to_linked_list(node=self.myList[theIndex], key=key, value=value)
        # increment the count of amount stored is in the input_to_linked_list function
        
    


    def input_to_linked_list(self, node, key, value):
        """
        This is the method that will put
        the item in the linked list
        if there is a link list present
        """
        if node.key == key:
            node.value = value
            return 
            
        if node.next == None:
            node.next = HashTableEntry(key, value)
            self.num_vals_entered +=1 # incrementing here for a new value
            return 
        
        return  self.input_to_linked_list(node=node.next, key=key, value=value)
        



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # to delete we will want to get the index and then find the key
        # will use a lot of the similar to get
        # the __getNode function will find the hash index
        val = self.__getNode(key, toDelete=True)
        if val[1] == None: # val is a tuple
            print(f"Waring, you cannot delete the key of {key} and value associated with it becuase they don't exist")
            return
        else:
            #doing the deleting of the node
            if val[0] == None: # this means there is no previous node
                # removing the next of val and making mylist to the next
                self.myList[self.hash_index(key)] = val[1].next
                val[1].next = None # this is to allow the garbage collection to happen to the value
            elif val[1].next == None:  # this would mean it is at the end
                val[0].next = None
            else:
                # the key, value pair is between other nodes
                val[0].next = val[1].next
                val[1].next = None
        self.num_vals_entered -= 1 # decrementing the amount

        # this is to resize the hash table when it is too empty
        # will only decrement to around 8 and then stop
        if (self.get_load_factor() <.2 and self.capacity < 8):
            self.resize(new_capacity=(self.capacity//2))







    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
     
        # getting first node
        val = self.__getNode(key)
        if val != None: 
            val = val.value
        return val


    def __getNode_recurs(self, node, key, toDelete , pevNode=None):
        """
        This is the function that will get the node for the 
        item.  Will return None if there is no node with the value and key 
        that is passed in.
        """
        if toDelete == False:
            if node == None:
                return None
            
            if node.key == key:
                return node
        elif toDelete == True:
            if node == None:
                return (None, None)
            if node.key == key:
                return (pevNode, node)
       
        return self.__getNode_recurs(node=node.next, key=key, toDelete=toDelete, pevNode=node)

    

    def __getNode(self, key, toDelete=False):
        """
        This is the function that will set up to use the 
        recursive getNode_recurs.  Will look to see if there
        is a link list in the index before calling the recursive function
        This method will return a tuple with the fist element being the previous node or
        none if there wasn't one.
        """
        theIndex = self.hash_index(key)
        bucket = self.myList[theIndex]
        if toDelete == True:
            if bucket == None:
                return (None, None)
        elif toDelete == False:
            if bucket == None:
                return None
        
        return self.__getNode_recurs(bucket, key, toDelete) # the head of the bucket will be the first node

        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # This is the function that will resize the hashtable 
        # make a list to hold the old values
        theOldlist = self.myList
        # making the new list
        self.myList = [None] * new_capacity
        self.capacity = new_capacity
        # setting the numbers used in the hash table
        self.num_vals_entered = 0

        # will now go through the old list
        for i in range(len(theOldlist)):
            headNode = theOldlist[i]
            if headNode == None:
                continue
            # going through each linked list

            while headNode != None:
                self.put(headNode.key, headNode.value)
                # now putting the headNode to the next node
                headNode = headNode.next

   




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
