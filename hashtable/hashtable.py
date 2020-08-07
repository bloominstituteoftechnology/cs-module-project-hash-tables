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
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.used_slots = 0


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
        hash = 5381

        for c in key:
            hash = (hash * 33) + ord(c) 
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

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # hash first the index,
        index = self.hash_index(key)

        # you will need to create a current pointer that points to the current item index
        cur = self.array[index]

        # if there is no item there, or if it is None, then you will just add that new 
        # HashTableEntry into that index
        # equal to the new HashTableEntry 
        if cur is None:

            self.array[index] = HashTableEntry(key, value)
            self.used_slots += 1
        else:
        # then you will want to do a next pointer that just is cur.next 
        # check first if there is an item already in that index, check it with if it's not None
        # if there is an item there, then call your .next from that current item and then make .next 
            while cur.next is not None: #and cur.key != key:
        # is refers to memory slot, a value is not guaranteed to be in memory slot
        # If you want to override a key's current value handle that case
        # if the key is equal to the current key we are on, then lets swap the current value with the 
        # value we want to input
                if cur.key == key:
                    cur.value = value
                    # print(f"You successfully overwritten the previous value")

                
                cur = cur.next

            if cur.key == key:

                cur.value = value
                print(f"You have overwritten the old value")

            else:
                cur.next = HashTableEntry(key, value)
                self.used_slots += 1
        # self.array[index] = HashTableEntry(key, value)


            


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.array[index]

        if cur is None:

            return f"Key Does Not Exist"
        else:
            
            while cur is not None:

                if cur.key == key:


                    old_value = cur.value
                    cur.value = None
                    return f"You deleted {old_value}"
                
                cur = cur.next

            return f"Key does not exist"
                

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.array[index]
        # print(index,'the index on get')
        # print(cur,'object at the index')
        
        if cur is None:
            # print(cur)
            return f"Key Does Not Exist in initial search"
        else:

            while cur is not None:
                
                if cur.key == key:

                    return cur.value
                else:
                    cur = cur.next
                
            return f"Key does not exist in traversed linked list"


        


        


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # if it is none don't add to new one 




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
