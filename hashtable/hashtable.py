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


    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.elements = 0

    def get_num_slots(self):
        
        return self.capacity



    def get_load_factor(self):
 
        return self.elements/self.capacity


    def fnv1(self, key):


        fnvPrime = 2**40 + 2**8 + 0xb3 # 64 bit prime
        hash = 14695981039346656037 #offset basis
        for i in key:
            hash *= fnvPrime
            hash = hash ^ ord(i)
        return hash & 0xFFFFFFFFFFFFFFFF

    def djb2(self, key):

        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):

        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):

        index = self.hash_index(key) 
        hst = HashTableEntry(key, value) 
        node = self.storage[index]
        

        if node is not None:
            self.storage[index] = hst
            self.storage[index].next = node
        else:
            self.storage[index] = hst
        self.elements +=1
        


    def delete(self, key):

        index = self.hash_index(key) 
        node = self.storage[index] 
        prev = None 

        if node.key == key:
            self.storage[index] = node.next
            return

        while node != None:
            if node.key == key:
                prev.next = node.next
                self.storage[index].next = None
                return

            prev = node
            node = node.next
        self.elements -=1
        return


    def get(self, key):

        index = self.hash_index(key)
        node = self.storage[index]

        if node is not None:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return node


    def resize(self, new_capacity):

        # Step 1: make a new, bigger table/array
        # ....Update capacity on new capacity
        # ....Update storage with new capacity
        prev_stor = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity
        # Step 2: go through all the old elements, and hash into the new list
        # Look through each key value pair in previous storage
        for i in range(len(prev_stor)):
            # Check previous storage with i as index
            old = prev_stor[i]
            # Check to see if that hash index exists:
            if old:
                # Look through this hash index list
                while old:
                    if old.key:
                        # If found, rehash to new storage
                        self.put(old.key, old.value)
                        # Continue looking through list until None
                        old = old.next
        



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
