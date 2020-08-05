class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.key}: {self.value}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, entry=0):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.entry = entry

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
        return self.entry / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass
        # Your code here

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
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Day 1
        # index = self.hash_index(key)
        # self.capacity[index] = value
        # print(index)

        # find index at given key
        # save it in a variable
        index = self.hash_index(key)
        cur = self.data[index]

        # if cur exists
        if cur:
            # loop thru the list by checking cur.next
            # and also see if cur.key is the same key
            # we're looking for
            while cur.next != None and cur.key != key:
                cur = cur.next
            # if there is already the key, overwrite the value
            if cur.key == key:
                cur.value = value
            # if key doesn't exists
            # make a new entry with cur.next
            # increase the entry, check for load factor
            else:
                cur.next = HashTableEntry(key, value)
                self.entry += 1

                if self.get_load_factor() > .7:
                    self.resize(self.capacity)

        # else, make new entry
        # increase entry count, check for load factor
        else:
            self.data[index] = HashTableEntry(key, value)
            self.entry += 1
            if self.get_load_factor() > .7:
                self.resize(self.capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # self.put(key, None)

        # find index at given key
        # save it in a variable
        index = self.hash_index(key)
        cur = self.data[index]

        # if value at index is empty
        if cur is None:
            return

        # else
        while cur:
            # if there is the same key
            # update the item with its next value
            # reduce the entry count
            if cur.key == key:
                self.data[index] = cur.next
                self.entry -= 1
            cur = cur.next

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # index = self.hash_index(key)
        # return self.capacity[index]

        index = self.hash_index(key)
        cur = self.data[index]

        # if cur exists
        while cur:

            # check for cur key
            # if exists, return value
            if cur.key == key:
                return cur.value

            # else, keep looping
            cur = cur.next

        # didn't find the value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        self.capacity = new_capacity

        # make a new table
        new_table = [None] * new_capacity

        # loop thru the old array
        for ll in self.data:
            cur = ll

            # if ll exists
            # get the key and hash it to get the index
            # for the new table
            while cur != None:
                index = self.hash_index(cur.key)

                # if position is None
                # set the key and value there
                if new_table[index] is None:
                    new_table[index] = HashTableEntry(cur.key, cur.value)

                # otherwise
                # loop thru that ll
                else:
                    new_cur = new_table[index]

                    # loop until the next node is None
                    if new_cur.next != None:
                        new_cur = new_cur.next

                    # if so, set the next node with the new key, value
                    new_cur.next = HashTableEntry(cur.key, cur.value)
                cur = cur.next

        # set self.data to the new table
        self.data = new_table


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
