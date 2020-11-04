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
        self.capacity = MIN_CAPACITY
        self.storage = [None] * capacity
        self.length = 0


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
        return self.length / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key: 
            hash = (( hash << 5)  + hash)+ ord(i)

        return hash & 0xffffffff 

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
        # index = self.hash_index(key)
        # self.storage[index] = value

        # the index is the spot where it's going
        index = self.hash_index(key)
        # node is the entry itself
        new_node = HashTableEntry(key, value)

        # keep track of the current node = head
        current_node = self.storage[index]

        # If this is the first node, create the node and increase the length to 1
        if current_node is None:
            self.storage[index] = new_node
            self.length += 1
            return 

        # as long as we aren't working with an empty or repeat node
        while current_node is not None and current_node.key != key:
            # the current node will now be the previous
            prev = current_node
            # we are making the current node the next one in line
            current_node = current_node.next
        
        # if we are working with an empty list, the new_node is now the previous node 
        if current_node is None:
            prev.next = new_node
            self.length += 1
        # otherwise assign the value to the current node    
        else:
            current_node.value = value

        # calculate the load factor
        load_factor = self.get_load_factor()

        # if the load factor is higher than 0.7 double the capacity
        if load_factor > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        if node.key == key:
            self.storage[index] = node.next
            self.length -= 1
            return 

        while node is not None and node.key != key:
            prev_node = node 
            node = node.next
        
        if node is None:
            return None

        prev_node.next = node.next
        self.length -= 1

        load_factor = self.get_load_factor()

        if load_factor < MIN_CAPACITY:
            self.resize(self.capacity)


        self.storage[index] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # keep track of the index of the hashtable
        index = self.hash_index(key)
        # return self.storage[index]

        # this is to keep track of the linked list inside each container
        node = self.storage[index]
        
        # we are going to loop through the entire linked list until we run out of entries
        # or we find a match
        while node is not None and node.key != key:
            # if we find a match then we assign the value of the next node to our node. 
            node = node.next
        # if we don't find the value we return none 
        # if we find it then we return the value
        return None if node is None else node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        for i in range(len(old_storage)):
            node = old_storage[i]

            while node is not None:
                index = self.hash_index(node.key)
                self.storage[index] = node
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
