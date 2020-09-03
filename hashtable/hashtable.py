import random

# Define a lookup table for the Pearson hash method
lookup = list(range(0, 256))
lookup = random.sample(lookup, 255)

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
        # Set the capacity for th hash table
        self.capacity = capacity
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY

        # Initialize the hash table
        self.table = [None]*self.capacity

        # Initialize a Person hash lookup table (for use in hashing keys)
        self.lookup = random.sample(list(range(0, 256)), 255)

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

    # hash_pearson returns the hash of an inbound message (string) based on the 
    #    given lookup table
    def hash_pearson(self, msg):
        # Initialize a hash value
        hsh = 0

        # Iterate over each character in the string
        for char in msg:
            # Generate the lookup value keyed of the current hash value xor'ed
            #   with unicode value of the current character
            hsh = self.lookup[hsh ^ ord(char)]

        # Done iterating: return the current hash value
        return hsh

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.hash_pearson(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Generate the hashed index of the inbound key
        idx         = self.hash_index(key)
        # Generate a new value node to be placed into the hash table
        new_node    = HashTableEntry(key, value)

        # Is the current table entry empty?
        if self.table[idx] == None:
            # Empty table entry, store the passed value as a new node
            self.table[idx] = new_node
            return

        # Have at least one node at this table index
        cur_node    = self.table[idx]
        while True:
            # Are we replacing an existing key/value pair (key == cur_node.key)
            if key == cur_node.key:
                # Yes, replace current node value with passed value
                cur_node.value = value
                return

            # Is this the last node?
            if cur_node.next == None:
                # at the last node in the linked list
                # append a new node referenced by a new key
                break

            # More nodes to traverse, advance to the next node
            cur_node = cur_node.next

        # Place new node at the end of the linked list
        cur_node.next = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Generate the hashed index of the inbound key
        idx = self.hash_index(key)

        # Is there a node at the index?
        if self.table[idx] == None:
            # No value associated with the key
            print("no value found associated with this hash key")
            return

        # One or more nodes exist at this index value
        last_node   = self.table[idx]
        cur_node    = self.table[idx]
        found_value = False
        while True:
            # Is the current node the node (droid) we're looking for?
            if cur_node.key == key:
                # Found our value
                found_value = True
                break

            # Is this the last node in the linked list
            if cur_node.next == None:
                # Last node, item not found
                break

            # Advance to the next node
            last_node = cur_node
            cur_node  = cur_node.next

        # Key not found?
        if not found_value:
            # key not found, message the user
            print("no value found associated with this hash key")
            return

        # Key has been found, delete the node
        # Linked list has only one node. Effectively delete the node
        if cur_node == last_node:
            # Remove the current node (first node)
            self.table[idx] = None
            return cur_node.value

        # Linked list has more than one node. Delete the pertinent (current) node
        last_node.next = cur_node.next
        return cur_node.value

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Generate the hashed index of the inbound key
        idx = self.hash_index(key)

        # Is there a node at the index?
        if self.table[idx] == None:
            # No value associated with the key
            return None

        # One or more nodes exist at this index value
        cur_node  = self.table[idx]
        while True:
            # Is the current node the node (droid) we're looking for?
            if cur_node.key == key:
                # Found our value
                return cur_node.value

            # Is this the last node in the linked list
            if cur_node.next == None:
                # Last node, item not found
                return None

            # Advance to the next node
            cur_node = cur_node.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Ensure the new capacity >= the minimum capacity
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY

        # Create a new list array
        new_table = [None]*new_capacity

        # Replicate the shared indexed values in the new list
        common_length = self.capacity
        if new_capacity <= common_length:
            common_length = new_capacity
        
        # Replicate the items in the common elements of the old and new table
        for idx, val in enumerate(self.table[:common_length]):
            new_table[idx] = val

        # Set the current table to old_table
        old_table = self.table

        # Set the instance table to the new table
        self.table = new_table  
        # Set the instance capacity to the new table's capacity
        self.capacity = new_capacity

        # Any more nodes to inspect?
        if len(old_table) > common_length:
            # Yes... inspect the rest of the nodes and rehash
            for jdx, jval in enumerate(old_table[common_length: len(old_table)]):
                # Node at this table location?
                if jval == None:
                    # No node found, skip
                    continue

                # Found a node. Rehash to the the updated table and capacity
                new_idx = self.hash_index(jval.key)
                # Set the node value to the new index in the object's table
                self.table[new_idx] = jval


