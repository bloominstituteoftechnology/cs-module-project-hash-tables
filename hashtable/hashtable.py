from llist import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.data = [None] * capacity
        self.items = 0
        # self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        a = self.capacity
        print(a)
        return a


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here            

        load = self.items / self.capacity
        # print(load)
        return load        

    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit
    #     Implement this, and/or DJB2.
    #     """
    #     # Your code here
    #     pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        # print(hash)
        return hash & 0xFFFFFFFF

        # key_bytes = key.encode()
        # hash = 5381
        # for k_byte in key_bytes:
        #     hash = hash * 33 + k_byte
        #     hash &= 0xffffffff
        # return hash

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

        # no collisions code
        # i = self.hash_index(key)
        # self.data[i] = value

        #  collisions resolution    
        i = self.hash_index(key)
        current_node = None

        if not self.data[i]:
            self.data[i] = HashTableEntry(key, value)
            self.items += 1
        else:
            current_node = self.data[i]

            while current_node.key != key and current_node.next:
                current_node = current_node.next

            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = HashTableEntry(key, value)
                self.items += 1
        l = self.get_load_factor()
        if l > 0.7:
            self.resize(self.capacity * 2)
            
        
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here

        # no collisions code
        # i = self.hash_index(key)
        # if i:
        #     self.data[i] = None
        # else:
        #     print('key not found')

        #  collisions resolution
        i = self.hash_index(key)
        previous_node = None
        current_node = self.data[i]

        if not current_node:
            return None        
                   
        while current_node.key != key and current_node.next:
            previous_node = current_node
            current_node = current_node.next

        if current_node.key == key and previous_node:
            previous_node.next = current_node.next                     
            deleted_value = current_node.value
            current_node.value = None            
            return deleted_value
        elif current_node.key == key:
            self.data[i] = current_node.next
        else:
            return 'key not found'
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here

        # no collisions code
        # i = self.hash_index(key)
        # if i:
        #     return self.data[i]
        # else:
        #     return None

        #  collisions resolution
        i = self.hash_index(key)
        current_node = self.data[i]

        if not current_node:
            return None

        while current_node.key != key and current_node.next:
            current_node = current_node.next

        if current_node.key == key:
            return current_node.value            
        else:
            return None                

        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        # i = self.hash_index(key)
        # new_hashtable = HashTable(capacity=new_capacity)
        old_storage = self.data
        new_storage = [None] * new_capacity
        self.data = new_storage
        self.capacity = new_capacity
        self.items = 0

        for node in old_storage:
            current = node
            # print(current.key)
            while current is not None:
                self.put(node.key, node.value)
                current = current.next        

        # if len(self.data) > self.capacity:
        #     self.capacity = new_capacity


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
