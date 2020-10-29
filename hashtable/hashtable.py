"""
UPER

Understand

Test cases:
    test_hashtable py module tests located in /hashtable folder, as well as at bottom of py module.


Plan: 

Single Linked List? - Higher possibility due to complexity state, which is contstant. *
Double Linked List? - Possible, but that invloves multiple lists attaching to one.
Binary Search Tree? - Also possible, but not sorting.

Normally a Set would reduce the list down to a managable size where no redundancy would be present,
However with the introduction of Linked List, it becomes a full stanza of mechanics.

I see it more as an autonomous function that requires little to no outside forces other than an input.

Look over Both.
Consider both as options.

Figure out Use Case and complexity.

CRUD application - Create(put) Read (get) Update (put) Delete (del)

Do Research on 64-LNV Hash. Will be located in Readme.md

Do Research on DJB2.

Impliment both, but only have one active at a time.

Apply both to Use Case.

Set up Hashing with Linked List use case.

Similar to usual Node Case.

Reminds of how Random Access Memory functions, using a base slot of 8 = Meaning 8 Bytes of code. 8 bits to a byte. 8 bytes to a nibble.

x64 bit run time. Not x64 Bytes.

Execute:
Code located below.

Review:

What worked and what didn't?

Complexity: Should be O(n) or at least O(n ^ 2)

"""


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# Constant - No additional flux for this statement. No lower than 8 slots.
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        """
        Set up Buckets, or storage containers. First clue is Buckets/Capacity.
        Capacity suggests maximum size, or n.
        """
        # Your code here
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.

        Length of Table.
        """
        # Your code here
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.

        I assume Load refers to how much work it needs to use.
        """
        # Your code here
        total = 0
        for index in range(len(self.table)):
            if self.table[index] is not None:
                current = self.table[index]
                while current is not None:
                    total += 1
                    current = current.next

        load = total/len(self.table)

        return load


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.

        I know it said choose one, I'm doing both.
        Research in Readme.md
        """

        # Your code here
        prime = 1099511628211
        offset = 14695981039346656037
        hash = offset

        for byte in key:
            hash = hash * prime
            hash = hash ^ ord(byte)

        return hash



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.

        I know it said choose one, I'm doing both.
        Research in Readme.md

        The easier one.
        """
        # Your code here
        hashDBJ2 = 5381
        for byte in key:
            hashDBJ2 = hashDBJ2 * 33 + ord(byte)

        return hashDBJ2

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.

        store = []
        Add value to store
        key has value
        access key, store value of key
        Find placement of key in index
        get key at position
        find value
        store value
        return value
        """
        # Your code here
        index = self.hash_index(key) # WHAT? BUILT IN???
        #save location in store
        store = self.table[index]
        # set up to launch record of the store, place as entry for recovery
        self.table[index] = HashTableEntry(key, value)
        # place in storage next location to continue on.
        self.table[index].next = store


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.

        Repeat insert, but in reverse.
        Use figures from Linked List for removing from list.
        Apply new head if needed.
        Apply new key to location if there are some after.
        """
        # Your code here
        index = self.hash_index(key) # set location

        # if Head
        # pointer = self.table[index] # set item
        # if pointer.key == key: # match item
        #     self.table[index] = pointer.next # skip item
        #     pointer.next = None 
        #     self.count -=1 # lower count

        #if not head

        # prev = self.table[index] # set Previous node/item
        # pointer = prev.next # set item as next in line
        # while pointer is not None: #if nothing after
        #     prev.next = pointer.next # make one to the other
        #     pointer.next = None # set it to nothing
        #     self.count -= 1 # reduce list
        #     return pointer # return the item itself.

        # return None
        if self.table[index].key == key:
            self.table[index] = None

        
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.

        Not too much different. Get the item itself.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.table[index]
        while entry:
            if entry.key == key:
                return entry.value
            else:
                entry = entry.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.

        Load needs to be called.
        Set new capacity
        set up doubling based on average size.
        figure out slots.
        set slot size.
        realize set minimum size = 8
        capacity is 8 minimum, no max size.
        Store current table as a different table.
        read old table and copy old table.
        check index location
        reset index location
        establish new table.
        count new number of slots
        put old table into new table.
        rewrite old table and new table into one.
        Bind lists
        1 = full
        0 = empty
        .1 to .9 is range amount between empty and full.
        """
        # Your code here
        # establish call to load
        load = self.get_load_factor()
        # reduce if load is small
        # set to minimum
        if load < 0.2: # if not filled much
            if self.capacity > 16: # doubled
                new_capacity = self.capacity/2 # 8
            else:
                return
        elif load > 0.7: # if filled close to complete
            new_capacity = 2 * self.capacity # double
        else:
            return
        if new_capacity < 8: # if more than minimum
            return # do nothing

        current_tab = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        #replace all info in old and write to new
        for i in range(len(current_tab)):
            current = current_tab[i]
            while current is not None:
                self.put(current.key, current.value)
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
