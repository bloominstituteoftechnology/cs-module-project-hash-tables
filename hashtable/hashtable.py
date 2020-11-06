# Import libraries, packages, modules needed:
import sys

# Constants:
HASH_TABLE_MIN_CAPACITY = 8
LOAD_FACTOR_MAX = 0.70
LOAD_FACTOR_MIN = 0.2
RESIZE_FACTOR = 2


class HashTableEntry:
    """
    Linked List node with hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    """
    Singly linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def find(self, key):
        """
        Find the given key if it exists in the LL, and return the node with that key (not only the value).
        """
        current = self.head
        # Cycle through LL nodes to find one with the key we're looking for:
        while current is not None:
            if current.key == key:
                return current
            else:
                current = current.next
        # If not found, return None:
        return None

    def insert_or_update(self, key, value):
        # Check if key is already in the LL:
        existing_node = self.find(key=key)
        # If it is already in the LL, then just update the value:
        if existing_node is not None:
            existing_node.value = value
        # Otherwise if not in the existing LL, add the value to the LL (as new node at head of LL):
        else:
            # Create node for new value:
            new_node = HashTableEntry(key=key, value=value)
            # Insert new node at head of list:
            new_node.next = self.head
            # Update head of LL to new node, and update LL length:
            self.head = new_node
            self.length += 1
            # If no existing tail (i.e., this is the only 1 node in this LL), set tail to new node too:
            if self.tail is None:
                self.tail = new_node


    def delete(self, key):
        prev = None
        current = self.head
        # Cycle through LL nodes to find one with the key we're looking for:
        while current is not None:
            next = current.next
            # If we find the key, remove that node from the LL (Python will then delete it from 
            # memory later because no remaining references to the node):
            if current.key == key:
                # If node is the head of the LL, update the head:
                if current is self.head:
                    self.head = current.next
                # If node is the tail of the LL, update the tail:
                if current is self.tail:
                    self.tail = prev
                # Connect any previous node to any next node in the LL, skipping over the node we are removing:
                if prev is not None:
                    prev.next = next
                current.next =  None
                # Update the LL's length:
                self.length -= 1
                return True
            else:
                prev = current
                current = current.next
        # If not found, return False:
        return False


class HashTable:
    """
    A hash table with `capacity` number of buckets
    that accepts string keys.
    """

    def __init__(self, capacity):
        self.capacity = max(capacity, HASH_TABLE_MIN_CAPACITY)
        self.array = [LinkedList() for slot in range(self.capacity)]


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
        full_slots = len(list(filter(lambda linkedlist: linkedlist.head is not None, self.array)))
        return full_slots / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        
        # Apply FNV-1 hash function to bytes representations:
        fnv_offset_basis = 14695981039346656037  # Same in hexadecimal: 0xcbf29ce484222325
        fnv_prime = 1099511628211  # = 2**40 + 2**8 + 0xb3, or in hex: 0x100000001b3
        hash_code = fnv_offset_basis
        for byte in key_as_bytes:
            # Faster C-style alt. syntax for the below: hash = ((hash << 5) + hash) + char
            hash_code *= fnv_prime
            hash_code = hash_code ^ byte
        
        return hash_code


    def djb2(self, key):
        """
        DJB2 hash function, 32-bit
        """
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        # Apply DJB2 hash function to bytes representations:
        hash = 5381
        for byte in key_as_bytes:
            # Faster C-style alt. syntax for the below: hash = ((hash << 5) + hash) + char
            hash = hash * 33 + byte
        
        return hash


    def djb2_xor(self, key):
        """
        DJB2 hash function, 32-bit
        """
        # Make sure key is a string (or can be converted to a string representation):
        try:
            key = str(key)
        except TypeError:
            sys.exit("Error: Please enter a string argument for 'key'.")
        
        # Get bytes representation of provided key:
        key_as_bytes = key.encode("utf-8")
        # Apply DJB2 hash function to bytes representations:
        hash = 5381
        for byte in key_as_bytes:
            # The ^ operator below is the bitwise XOR operator:
            hash = ((hash * 33) ^ byte)  # Q: Should we then % 128 (same as % 0x10000000) this to "keep it 32-bit" bc "python ints don't overflow"?
        
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        hash_code = self.djb2(key)

        # Modulo the result to make sure it is an index within the existing array:
        return hash_code % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions handled with Linked List Chaining.
        """
        # Get index for this key from our hash function:
        index = self.hash_index(key)
        # Get the LL at that index (even if it is empty, i.e., has no nodes):
        LL = self.array[index]
        # Check if this key is already in the LL at this index. If so, update it. 
        # If not, add a node with this key:value pair to the LL at this index:
        LL.insert_or_update(key=key, value=value)

        # Resize if needed:
        if self.get_load_factor() > LOAD_FACTOR_MAX:
            self.resize(new_capacity = RESIZE_FACTOR * self.capacity)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Get index for this key from our hash function:
        index = self.hash_index(key)
        # Get the LL at that index (even if it is empty, i.e., has no nodes):
        LL = self.array[index]
        # Check if this key is in the LL at this index. If so, delete it.
        LL.delete(key=key)

        # Resize if needed:
        if self.get_load_factor() < LOAD_FACTOR_MIN:
            self.resize(new_capacity = max(self.capacity // RESIZE_FACTOR, HASH_TABLE_MIN_CAPACITY))


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Get index for this key from our hash function:
        index = self.hash_index(key)
        # Get the LL at that index (even if it is empty, i.e., has no nodes):
        LL = self.array[index]
        # Check if this key is in the LL at this index. 
        node = LL.find(key=key)
        # If it is (returned node is not None), return the associated value:
        if node is not None:
            return node.value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # Create new array of the right size:
        new_array = [LinkedList() for slot in range(new_capacity)]
        # Update capacity here first, because it is used in hash_index() method:
        self.capacity = new_capacity

        # Re-hash every element in old array --> add at the resulting index of new array:
        for num, linkedlist in enumerate(self.array):
            current_node = linkedlist.head
            # Add keys, values in the current LL to new array:
            while current_node is not None:
                # Get each key and value:
                key, value = current_node.key, current_node.value
                #  Hash the key to get insert index for new array --> get the LL at that index (even if LL has no nodes):
                LL = new_array[self.hash_index(key)]
                # Add key, value to the LL (at the right index in the new array):
                LL.insert_or_update(key=key, value=value)
                # Increment: Move to next node in LL:
                current_node = current_node.next
        # Update the hash table's underlying array to the new array:
        self.array = new_array


# # To test:
# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
