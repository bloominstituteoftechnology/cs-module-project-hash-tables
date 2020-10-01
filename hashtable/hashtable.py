class Node:
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
        self.capacity = capacity;
        self.size = 0;
        self.slots = [None]*self.capacity;

    def get_num_slots(self): return len(self.slots)
    def get_load_factor(self): return self.size / len(self.slots)

    def checkCapacity(self):
        self.size += 1 #size ++ 
        if self.size/self.capacity > .7:
            self.resize(self.capacity*2)
        else:
            return

    def fnv1(self, key):
        # FNV-1 Hash, 64-bit
        hsh = 14695981039346656037; # 64bit ( &= 0xcbf29ce484222325 ) or ( 14695981039346656037 )
        fnv_prime = 1099511628211; # 64bit (240 + 28 + 0xb3) or ( 1099511628211 )

        for char in key:
            hsh = hsh * fnv_prime 
            hsh = hsh ^ ord(char)

        return hsh

    def djb2(self, key):
        # DJB2 hash, 32-bit
        hsh = 5381

        for char in key:
            hsh = (( hsh << 5) + hsh) + ord(char)

        return hsh & 0xFFFFFFFF


    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index
        # between within the storage capacity of the hash table.

        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        idx = self.hash_index(key)  # hash index
        node = self.slots[idx]      # ref slot @ index
        precursor = node            # 2nd ref in case prexisting node
        # Empty Slot? ->
        # Insert node!
        if node is None:
            self.slots[idx] = Node(key,value)
            self.checkCapacity()
            return
        # Occupied? ->
        # Loop through occupants looking for key or back of the list
        while node != None:
            # Key match?
            if key == node.key:
                # replace value!
                node.value = value
                return
            precursor = node
            node = node.next

        precursor.next = Node(key,value)
        self.checkCapacity()

    def get(self, key):
        idx = self.hash_index(key)
        node = self.slots[idx]
        
        # Node has next and node key doesn't match?
        # Loop until we are at the back of the list!
        while node is not None and node.key != key:
            node = node.next
		# Noting here? Return None. :( 
        if node is None:
            return None
        # Found it? Great! Return vale!
        else:
            return node.value 

    def delete(self, key):
        idx = self.hash_index(key)    # hash index
        node = self.slots[idx]  # ref slot @ index
        prev = None               # previous node ( might need to itterate a list @ slot )
		# Find something? No key match?
        # Ref current as previous and next as current! Loop until end of list!
        while node is not None and node.key != key:
            prev = node
            node = node.next
		# Find something?
        # Cool, kill, death, fire.
        if node is not None:
            self.size -= 1
            # If we are at the head of the list just set the new head as the next node
            if prev is None: self.slots[idx] = node.next
            # If we aren't at the head set the previous nodes new next to current next
            else: prev.next = prev.next.next
            return node.value
        # Nothing to delete? Return None. :(
        else: return None

    def printAll(self):
        numSlots = self.get_num_slots()-1
        last = self.slots[numSlots]
        while (last == None):
            if numSlots < 0: return False
            else:
                self.delete(last.id)
                return True

    def resize(self, new_capacity):
        newTable = HashTable(new_capacity)
        num = (self.capacity  - 1)
        clone = self.clone( num , newTable )
        self.capacity = clone.capacity
        self.size = clone.size
        self.slots = clone.slots
        # Your code here

    def clone(self, num, table):
        while self.size > 0:
            item = self.slots[num]

            if item != None:
                table.put(item.key, item.value)
                self.delete(item.key)
                return self.clone(num, table)
            else:
                return self.clone(num - 1, table)

        return table


"""
print(f"capacity = {ht.capacity} ===========================================================")
print(f"size = {ht.size} =================================================================")
print(f"len = {len(ht.slots)} ===========================================================")
"""

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

