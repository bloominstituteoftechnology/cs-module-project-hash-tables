

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"(key: {self.key} value: {self.value})"




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
        self.table = [None] * capacity
        self.count = 0
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        number_of_slots = len(self.table)
        total_num_of_items = self.count
        load_factor = total_num_of_items / number_of_slots
        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hashbrown = 14695981039346656037
        bytes_of_data = key.encode()
        for i in bytes_of_data:
            hashbrown = hashbrown ^ i
            hashbrown = hashbrown * 1099511628211 
        return hashbrown

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
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        # Your code here
        print(index)
        if(self.table[index] != None):
            if(self.table[index].key == key):
                head = HashTableEntry(key, value)
                head.next = self.table[index].next
                self.table[index] = head
                
            else:
                head = HashTableEntry(key, value)
                head.next = self.table[index]
                self.table[index] = head
                self.count += 1
        else:
            self.table[index] = HashTableEntry(key, value)
            self.count += 1
        
        if (self.get_load_factor() > 0.7):
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        
        if(self.table[self.hash_index(key)] == None):
            return None

        if(self.table[self.hash_index(key)].key == key):
            old_head = self.table[self.hash_index(key)]
            
            self.table[self.hash_index(key)] = self.table[self.hash_index(key)].next
            old_head.next = None
            self.count -= 1
            return old_head
        prev = self.table[self.hash_index(key)]
        curr_node = self.table[self.hash_index(key)].next

        while(curr_node is not None):
            if(curr_node.key == key):
                prev.next = curr_node.next
                curr_node = None
                self.count -= 1
                return curr_node
            prev = prev.next
            curr_node = curr_node.next

        return "Key is not found"
        # Your code here
        
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        print(f"\n {self.table} \n")
        print(f"\n {self.hash_index(key)} \n")
        index = self.hash_index(key)
        
        if(self.table[index] == None):
            return None
        else:
            curr_node = self.table[index]
            while(curr_node != None):
                if(curr_node.key == key):
                    return curr_node.value
                curr_node = curr_node.next
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        table_to_add = [None]*new_capacity
        copy_of_table = self.table.copy()
        self.table = table_to_add
        self.capacity = new_capacity

        # do this after implementing linked list chaining
        for i in range(len(copy_of_table)):
            curr_node = copy_of_table[i]
            if(curr_node == None):
                pass
            elif(curr_node != None):
                while(curr_node != None):
                    self.put(curr_node.key, curr_node.value)
                    curr_node = curr_node.next
            else:
                self.put(curr_node.key, curr_node.value)
                


            


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
