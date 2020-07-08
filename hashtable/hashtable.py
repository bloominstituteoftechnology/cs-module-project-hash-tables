class HashTableEntry:
    #this is day two work
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head

        while current:
            if current.value == value:
                return current
            current = current.next

    def delete(self, value):
        current = self.head

        #if the item to delete is the head
        if current.value == value:
            self.head = current.next

        prev = current
        current = current.next

        while current:
            if current.value == value:
                prev.next = current.next
                return current
            else:
                prev = current
                current = current.next
        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

#keeping track of how many items in hash table with global var
items_in_hashtable = 0


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY
        self.hash_table = [None] * self.capacity

    def __str__(self):
        return f'{self.hash_table}'

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        global items_in_hashtable

        load_factor = items_in_hashtable / self.get_num_slots()

        return load_factor


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
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

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

        key_sum = self.hash_index(key)
        entry = HashTableEntry(key, value)

        global items_in_hashtable

        #save this long name
        hashed_key_spot = self.hash_table[key_sum]
    
        #if there is not a list set up at this value
        if not hashed_key_spot:
            #initiate list
            hash_list = LinkedList()

            #use list function to insert node
            hash_list.insert_at_head(entry)

            #save the list to the spot in the hash
            #hashed_key_spot = hash_list
            self.hash_table[self.hash_index(key)] = hash_list
            items_in_hashtable += 1
            return f'Inserted {self.hash_table[self.hash_index(key)].head.value}'

        else:
            self.hash_table[self.hash_index(key)].insert_at_head(entry)
            items_in_hashtable += 1
            return f'Inserted {value}'

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        global items_in_hashtable
        key_hashed = self.hash_table[self.hash_index(key)]

        deleted = key_hashed.head.value

        # self.hash_table[key_hashed] = None
        current = key_hashed.head
        if key_hashed:
            while current:
                if current.key == key:
                    key_hashed.delete(key_hashed.head.value)
                    items_in_hashtable -= 1
                    return f'{deleted} has been deleted from the hash table.'
                current = current.next
            return f'Could not find {key} in hash table.'


        #hash key
        #go to hash
        # check if key matches unhashed key
        # if so, reweave pointers accordingly (if head, if not head)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #key_hashed = self.djb2(key) % self.capacity

        hashed_key = self.hash_table[self.hash_index(key)]
        current = hashed_key.head

        if hashed_key:
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return f'Could not find {key} in hash table.'



    def resize(self, new_capacity):
        #this is technically for tomorrows work
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() > 0.7:

            new_hash = HashTable(self.capacity)

            for i in self.hash_table:
                current = i.head
                while current:
                    new_hash.put(i.head.key, i.head.value)
                    current = current.next

                new_hash.put(i.head.key, i.head.value)
            return new_hash
        return 'There is not yet a need to resize.'


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
    print('Storing all lines beyond capacity:')
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

    # print('The hashtable:')
    # print(ht)

    # print('Get line five:', ht.get("line_5"))

    # print('Delete line five:', ht.delete("line_5"))
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
        
    print(ht.get_load_factor())

    print(ht.get_num_slots())