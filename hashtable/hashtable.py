class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedHash:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def tail_add(self, key, value):
        new_entry = HashTableEntry(key, value, None)
        
        # There is a tail
        if self.tail:
            self.tail.next = new_entry

        # There in No tail
        else: 
            self.head = new_entry
        
        # In either case
        self.tail = new_entry
    
    def search(self, key):
        if not self.head:
            return None
        
        else:
            checkingnode = self.head

            while checkingnode is not None:
                if checkingnode.key == key:
                    return checkingnode

                else:
                    pass
                checkingnode = checkingnode.next

            return None
    
    def delete(self, key):
        checkingnode = self.head

        # Empty list case
        if checkingnode is None:
            return None
        
        # List with one object case
        elif self.head == self.tail:
            delkey = self.head.key
            self.head = None
            self.tail = None
            return delkey
        
        # Deleting head case
        elif self.head.key == key:
            delkey = self.head.key
            next_head = self.head.next
            self.head = next_head
            return delkey
        
        # Deleting tail case
        elif self.tail.key == key:
            delkey = self.tail.key

            while checkingnode.next != self.tail:
                checkingnode = checkingnode.next
            
            delkey = self.tail.key
            self.tail = checkingnode
            return delkey
        
        # Deleting anything else
        else:
            prev = checkingnode
            checkingnode = checkingnode.next

            while checkingnode is not None:
                if checkingnode.key == key:
                    prev.next = checkingnode.next_head
                    return checkingnode
                
                else:
                    prev = checkingnode
                    checkingnode = checkingnode.next
            
            return None

        
            



class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):

        if capacity > MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY

        # self.hash = LinkedHash() * capacity
        self.hash = [LinkedHash() for i in range(capacity)]
        self.obj_counter = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.# Your code here
        """
        # print('The Capacity of this HashTable is:', self.capacity)
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        loadfactor = self.obj_counter/self.capacity

        return loadfactor


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
        hash = 5381 # this is one of the magic dfb2 numbers
        for c in key:
            hash = ((hash << 5) + hash) + ord(c)
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

        Hash # Your code herecollisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        hashlist = self.hash[index]
        checkobject = hashlist.search(key)

        if checkobject == None: # new key
            self.hash[index].tail_add(key, value)
            self.obj_counter +=1
        
        else: # overwrite
            checkobject.value = value


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        hashlist = self.hash[index]
        getobject = hashlist.search(key)

        if getobject == None:
            return None
        
        else:
            return getobject.value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        hashlist = self.hash[index]
        hashlist.delete(key)


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # if self.get_load_factor() > 0.7:
            # newcap = self.capacity * 2
        oldhash = self.hash.copy()
        self.__init__(new_capacity)

        for i in oldhash:
            checkingnode = i.head
            while checkingnode is not None:
                self.put(checkingnode.key, checkingnode.value)
                checkingnode = checkingnode.next
            


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")# Your code here
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the language:english$mome raths outgrabe.")
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