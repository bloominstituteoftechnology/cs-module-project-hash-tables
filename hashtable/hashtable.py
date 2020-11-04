
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_value(self):
        return self.value
    
    def get_key(self):
        return self.key


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
        self.hashTable = [None] * capacity
        

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
        item_count = 0
        for item in self.hashTable:
            if item is not None:
                if item.next:
                    current = item
                    while current:
                        item_count += 1

                        if current.next is not None:
                            current = current.get_next()
                        
                        else:
                            break
                else: 
                    item_count += 1

            # print(" - - - -")
            # print(item_count)
                     
        return item_count / self.get_num_slots()

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
        # Your code here
        index = self.hash_index(key)
        entry = HashTableEntry(key, value)

        # check if there is something at that index
        if self.hashTable[index] is not None:
            current_node = self.hashTable[index]
            if current_node.key == key:
                print("first node has same key")
                current_node.value = value
            else:
                while current_node:
                    if current_node.get_key() == key:
                        current_node.value = value
                        break
                        
                    if current_node.next is not None:
                        print(current_node.next.key)
                        current_node = current_node.get_next()
                    else: 
                        current_node.next = entry
                        break
                    
        else:
            self.hashTable[index] = entry

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        #self.hashTable[index] = None
        if self.hashTable[index]:
            current_node = self.hashTable[index]
            # if current_node.key == key:
            #     self.hashTable[index] = None
            #     return None
            
            if current_node.next is not None:
                while current_node:
                    if current_node.get_key() == key:
                        refrence = self.hashTable[index].next
                        self.hashTable[index] = None
                        self.hashTable[index] = refrence
                        return None
                        
                    if current_node.next is not None:
                        current_node = current_node.get_next()
                    else: 
                        return None
            else: 
                if current_node.get_key() == key:
                    self.hashTable[index] = None
                    return None
        else: 
            return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if self.hashTable[index]:
            # check if has next
            current_node = self.hashTable[index]
            if current_node.next is not None:
                while current_node:
                    if current_node.get_key() == key:
                        return current_node.value
                        
                    if current_node.next is not None:
                        current_node = current_node.get_next()
                    else: 
                        return None
            else: 
                if current_node.get_key() == key:
                    return current_node.value

        else:
            return None

    def resize(self,new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # self.capacity *= 2
        self.capacity = new_capacity
        blank_array = [None] * new_capacity
        for item in self.hashTable:
            if item is not None:
                if item.next is not None:
                    # reHashed = self.hash_index(item.key)
                    current = item
                    while current:
                        reHashed = self.hash_index(current.key)

                        # doing the put method here basically
                        if blank_array[reHashed] is not None:
                            current_node = blank_array[reHashed]
                            
                            while current_node:
                                # checking to see if has the same key
                                if current_node.get_key() == current.key:
                                    current_node.value = current.value
                                    break
                                
                                # checking if we are still not at the end of the linked lsit
                                if current_node.next is not None:
                                    current_node = current_node.get_next()
                                else: 
                                    current_node.next = HashTableEntry(current.key, current.value)

                        else: 
                            blank_array[reHashed] = HashTableEntry(current.key, current.value)

                        if current.next is not None:
                            current = current.next
                        else:
                            break

                else:
                    reHashed = self.hash_index(item.key)
                    blank_array[reHashed] = HashTableEntry(item.key, item.value)

        # print(" - - - - - -")
        # for x in blank_array:
        #     if x is not None:
        #         print(x.key)
        #         if x.next is not None:
        #             print("+ + +")
        #             print(x.next.key)
        #     else: 
        #         print("none")

        self.hashTable = None
        self.hashTable = blank_array
            


new_table = HashTable(8)

new_table.put("key-0", "val-0")
new_table.put("key-1", "val-1")
new_table.put("key-2", "val-2")
new_table.put("key-3", "val-3")
new_table.put("key-4", "val-4")
new_table.put("key-5", "val-5")
new_table.put("key-6", "val-6")
new_table.put("key-7", "val-7")
new_table.put("key-8", "val-8")
new_table.put("key-9", "val-9")
new_table.put("key-10", "val-10")
new_table.put("key-11", "val-11")
new_table.put("key-12", "val-12")
new_table.put("key-13", "val-13")
new_table.put("key-14", "val-14")
new_table.put("key-15", "val-15")
new_table.put("key-16", "val-16")
new_table.put("key-17", "val-17")
new_table.put("key-18", "val-18")
new_table.put("key-19", "val-19")
new_table.put("key-20", "val-20")
print(" - - - - - -")
print(len(new_table.hashTable))
for x in new_table.hashTable:
    if x is not None:
        print(x.key)
        if x.next is not None:
            print("+ + +")
            print(x.next.key)
            print("+ + +")
        else: 
            print("none")

# new_table.resize()


# for x in new_table.hashTable:
#     print(x.key)

# new_table.delete("key-7")
# new_table.delete("key-6")
# new_table.delete("key-5")
# new_table.delete("key-4")
# new_table.delete("key-3")
# new_table.delete("key-2")
# new_table.delete("key-1")
# new_table.delete("key-0")

# print("/n")
# for x in new_table.hashTable:
#     print(x.key)



if __name__ == "__main__":
    ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
