class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    def find(self, key):
        current = self.head

        while current:
            if current.key == key:
                return current
            current = current.next

    def insert_at_head(self, key, value):
        # Check if key is already there, update
        # else make a new one
        if self.find(key):
            found = self.find(key)
            found.value = value
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node



# One way to handle collisions is Open addressing :linear probing, just add your info in the next X available slot
# We will do linked lists, node has key and value
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = max(MIN_CAPACITY, capacity)
        self.hash_map = [None] * self.capacity


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
        # Your code here
        # number items in hash table / number of slots
        items = 0
        for element in self.hash_map:
            current = element
            while current:
                items += 1
                current = current.next
        load_factor = items / self.capacity

        return load_factor

    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        hash = offset_basis
        for each octet_of_data to be hashed
            hash = hash * FNV_prime
            hash = hash xor octet_of_data
            return hash
        https://github.com/sup/pyhash/blob/master/pyhash/pyhash.py
        """
        fnv_prime = 1099511628211 # prime number with a bunch of other rules
        offset_basis = 14695981039346656037 # based on the size of the hash, 64-bit
        hash = offset_basis + seed
    
        for char in key:
            hash = hash * fnv_prime
            hash = hash ^ ord(char) # This XOR gate will compare each binary digit, 110 vs 100 = 011 true if 1 and only one
        return hash
        # Could also use string_bytes = key.encode(). Loop through that and just have hash ^ char


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        # in both: choose big random number, usually prime. Loop over bytes of string, due something hard to predict
        pass


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        
        return self.fnv1(key) % self.capacity
        

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)

        if not self.hash_map[hash_index]: # Nothing there, put a node
            self.hash_map[hash_index] = HashTableEntry(key, value)

        else:
            current_node = self.hash_map[hash_index]

            while current_node.key != key and current_node.next:
                current_node = current_node.next
            # update existing
            if current_node.key == key:
                current_node.value = value
            else:
                current_node.next = HashTableEntry(key, value) # add at end
        if self.get_load_factor() > 0.7:
            self.resize(2*self.capacity)
    


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.hash_map[hash_index]:
            current_node = self.hash_map[hash_index]
            prev = current_node
            while current_node.key != key and current_node.next:
                prev = current_node
                current_node = current_node.next
            # update existing
            if current_node.key == key:
                prev.next = current_node.next
                current_node.value = None
        else:
            print("Error: key not found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if self.hash_map[hash_index]:
            current_node = self.hash_map[hash_index]

            while current_node.key != key and current_node.next:
                current_node = current_node.next
            # update existing
            if current_node.key == key:
               return current_node.value
        # else:
        #     return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        # change capacity
        # iterate through old array and linked lists
            # add  everything to new list
        old_hash_map = self.hash_map
        self.hash_map = [None] * new_capacity
        self.capacity = new_capacity

        for element in old_hash_map:
            current = element
            while current:
                self.put(element.key, element.value)
                current = current.next



        



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