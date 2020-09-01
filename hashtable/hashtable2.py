class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.id = key
        self.value = value
        self.next = None
        self.prev = None
    
    def isAlone(self):
        if (self.prev is None):
            return True
        else:
            return False

    def die(self):
        if (self.next and self.prev):
            self.next.prev = self.prev;
            self.prev.next = self.next;
        elif (self.next):
            self.value = self.next.value;
            self.id = self.next.id;
            self.next = None;
        elif (self.prev):
            self.prev.next = None;
        else: 
            print('this node must be killed from the table')


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity;
        self.size = 0;
        self.slots = [None]*self.capacity;

    def get_num_slots(self): return len(self.slots)
    def get_load_factor(self): return self.size / len(self.slots)

    def fnv1(self, key):
        # FNV-1 Hash, 64-bit
        hsh = 14695981039346656037; # 64bit ( &= 0xcbf29ce484222325 ) or ( 14695981039346656037 )
        fnv_prime = 1099511628211; # 64bit (240 + 28 + 0xb3) or ( 1099511628211 )
        #print(key)
        for char in key:
            hsh = hsh * fnv_prime 
            hsh = hsh ^ ord(char)

        return hsh

    def djb2(self, key):
        # DJB2 hash, 32-bit
        hsh = 5381

        for char in key:
            hsh = (( hsh << 5) + hsh) + ord(char)

        #print(f' hashing key: {key} to {hsh & 0xFFFFFFFF % self.capacity}')
        return hsh & 0xFFFFFFFF

    def findInSlot(self, key):
        precursor = self.slots[self.hash_index(key)] #precursor = first item indexed in this slot
        while precursor.next != None and precursor.id != key: # itterate until current key is found or end of the linked list
                precursor = precursor.next
        return precursor #return end of linked list

    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index
        # between within the storage capacity of the hash table.

        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def isSlotEmpty(self, key):
        if self.slots[self.hash_index(key)] is None: return True
        else: return False

    def put(self, key, value):
        if(self.isSlotEmpty(key)):
            self.size += 1 # increment size
            self.slots[self.hash_index(key)] = HashTableEntry(key, value); # Store the value with the given key.
        else:
            precursor = self.findInSlot(key)

            if precursor.id == key:
                precursor.value = value;
                #print('overwrite detected')
            else:
                precursor.next = HashTableEntry(key, value) # append current item as next
                precursor.next.prev = precursor
                #print('collision detected')

        #print(f'value = {value} and key = {key}')    
        self.size += 1

        if (self.get_load_factor() >= .7): 
            self.resize(self.get_num_slots()*2)

    def delete(self, key):
        if (self.isSlotEmpty(key)): print("Invalid key input.");
        else:
            if self.findInSlot(key).isAlone(): # Remove the value stored with the given key.
                self.slots[self.hash_index(key)] = None
            else:
                self.findInSlot(key).die()
            self.size -= 1; # decrement size

    def get(self, key):
        if (self.isSlotEmpty(key)):
            #print("Invalid key input.");
            return None # Returns None if the key is not found.
        else:
            print(f'returning key: {key} as {self.findInSlot(key).value}')
            return self.findInSlot(key).value; # Return the value stored with the given key.

    def resize(self, newSize):
        """
        
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new = HashTable(newSize)
        isTableItems = True
        while isTableItems:
            isTableItems = self.convert(new)

        self = new;
        isTableItems = True
        while isTableItems:
            isTableItems = self.printAll()

    def convert(self, newTable):
        numSlots = self.get_num_slots()-1
        last = self.slots[numSlots]
        while (last == None):
            if numSlots < 0: return False
            else:
                numSlots -= 1
                last = self.slots[numSlots]

        #print(self.get_num_slots()-1)
        print(f'converting {last.id} ---------------------------------------------------------------------------------------------------')
        if (last):
            newTable.put(last.id, last.value)
            self.delete(last.id)
            return True

    def printAll(self):

        numSlots = self.get_num_slots()-1
        last = self.slots[numSlots]
        while (last == None):
            if numSlots < 0: return False
            else:
                print(f'Key:{last.id} , Value: {last.value}')
                self.delete(last.id)
                return True


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
