import random

# Define a lookup table for the Pearson hash method
lookup = [44,
    152,
    117,
    52,
    116,
    140,
    151,
    225,
    29,
    170,
    204,
    22,
    122,
    88,
    121,
    83,
    183,
    158,
    230,
    9,
    203,
    77,
    124,
    172,
    238,
    213,
    63,
    35,
    169,
    62,
    23,
    164,
    19,
    235,
    236,
    248,
    149,
    174,
    24,
    92,
    249,
    98,
    68,
    41,
    176,
    212,
    81,
    135,
    49,
    194,
    177,
    254,
    224,
    167,
    53,
    202,
    96,
    244,
    10,
    69,
    188,
    133,
    21,
    118,
    65,
    93,
    40,
    250,
    85,
    157,
    46,
    20,
    205,
    218,
    55,
    73,
    246,
    94,
    8,
    137,
    72,
    99,
    102,
    255,
    144,
    142,
    106,
    108,
    187,
    226,
    12,
    42,
    89,
    75,
    105,
    129,
    112,
    146,
    231,
    56,
    59,
    54,
    165,
    190,
    191,
    50,
    222,
    39,
    200,
    5,
    182,
    27,
    67,
    17,
    57,
    247,
    150,
    228,
    210,
    195,
    66,
    239,
    163,
    159,
    185,
    243,
    208,
    252,
    171,
    198,
    2,
    173,
    126,
    184,
    139,
    234,
    3,
    26,
    128,
    82,
    58,
    214,
    33,
    196,
    113,
    48,
    245,
    178,
    237,
    125,
    189,
    166,
    111,
    107,
    34,
    232,
    162,
    217,
    207,
    127,
    161,
    18,
    131,
    103,
    199,
    80,
    91,
    223,
    148,
    78,
    51,
    145,
    241,
    31,
    153,
    141,
    16,
    115,
    216,
    60,
    251,
    156,
    123,
    95,
    215,
    154,
    109,
    97,
    70,
    132,
    79,
    14,
    136,
    43,
    119,
    186,
    180,
    74,
    181,
    76,
    138,
    47,
    242,
    168,
    28,
    227,
    114,
    45,
    206,
    130,
    36,
    38,
    71,
    147,
    30,
    155,
    160,
    220,
    84,
    233,
    253,
    211,
    175,
    1,
    90,
    4,
    7,
    101,
    219,
    179,
    240,
    32,
    134,
    100,
    13,
    193,
    64,
    197,
    201,
    221,
    229,
    37,
    86,
    104,
    143,
    11,
    87,
    25,
    209,
    15,
    120,
    6,
    61,
    192,
    110]


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
        self.lookup = lookup

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

            # Key not found. Is this the last node in the linked list
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
        # At what position are we in the linked list?
        # Linked list has only one node: it is the current, last, and only node
        if cur_node == last_node and cur_node.next == None:
            # Remove the current node (first node)
            self.table[idx] = None
            return

        # Last node of a list with more than one node
        if last_node != cur_node and cur_node.next == None:
            # current node is the last node of a list with >1 nodes
            # remove last node
            last_node.next = None
            return

        # Interim node of a list with more than two nodes
        if last_node != cur_node and cur_node.next != None:
            last_node.next = cur_node.next
            return

        # First node of a list with more than one node
        #* PICK UP HERE!!!!
        if last_node == cur_node and 



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


