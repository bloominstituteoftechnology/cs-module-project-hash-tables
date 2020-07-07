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
        self.data = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.size/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here
        seed = 0
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


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
        # Your code here
        # slot = self.hash_index(key)
        # entry = HashTableEntry(key, value)
        # self.capacity[slot] = entry

        index = self.hash_index(key)
        if(self.data[index] == None):
            self.data[index] = HashTableEntry(key, value)
            self.size +=1
        else:
            #check if it exists 
            curr = self.data[index]
            while curr.next and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            #it doesn't exist, so add it to the head of the list
            else:
                curr.next = HashTableEntry(key, value)
                self.size +=1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2 )


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # self.put(key, None)

        index = self.hash_index(key)
        #node to delete was first in list
        if self.data[index].key == key:
            #if it was only one in the list
            if self.data[index].next == None:
                #list should now be empty
                self.data[index] = None
                self.size -=1
            #it is not the only one in the list
            else:
                new_head = self.data[index].next
                self.data[index].next = None
                self.data[index] = new_head
                self.size -=1
        #node was not first in the list or is none
        else:
            if self.data[index] == None:
                return None
            else:
                curr = self.data[index]
                prev = None
                #search until at end or have found key
                while curr.next is not None and curr.key != key:
                    prev = curr
                    curr = curr.next
                #found the key
                if curr.key == key:
                    prev.next = curr.next
                    self.size -=1
                    return curr.value
                #didn't find the key
                else:
                    return None

        if self.get_load_factor() < 0.2:
            self.resize(max(self.capacity // 2, MIN_CAPACITY))


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # entry = self.capacity[slot]

        # if entry:
        #     return entry.value
        # return None

        index = self.hash_index(key)
        #if it is the first thing in the ll
        if self.data[index] is not None and self.data[index].key == key:
            return self.data[index].value
        #there's nothing there to get
        elif self.data[index] is None:
            return None
        #possibly later in the ll
        else:
            curr = self.data[index]
            while curr.next != None and curr.key != key:
                curr = self.data[index].next
            if curr == None:
                return None
            else:
                return curr.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        curr = self.data
        self.capacity = new_capacity
        self.data = [None] * new_capacity

        for i in curr:
            if i: 
                node = i 
                while node:
                    self.put(node.key, node.value)
                    node = node.next




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
    print(ht.get_load_factor())