class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # use this to find the node in the hash table.
    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def insert_at_head(self, key, value):
        n = HashTableEntry(key, value)
        n.next = self.head
        self.head = n

    def delete_node(self, key):
        cur = self.head
        if cur.key == key:
            self.head = self.head.next
            cur.next = None
            return cur
        # general cases
        prev = cur
        cur = None

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None


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
        self.capacity = [None] * capacity
        self.count = 0
        self.storage = [LinkedList()] * capacity

        self.capacity = [None] * MIN_CAPACITY

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # number of items in the hash table divided by the capacity
        # Your code here
        total_items = self.count
        cap = self.get_num_slots()
        return total_items / cap

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        #

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
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
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #   Find the index in the hash table for the key
        # * Search the list at that index for the key
        # * If it exists:
        #   * Overwrite the value
        # * Else it doesn't exist:
        #   * Make a new record (`HashTableEntry` class) with the key and value
        #   * Insert it anywhere in the lis
        self.count += 1

        # checking to see if the key exsists
        if self.capacity[self.hash_index(key)] is not None:
            # since it does we want to
            # overwrite value
            overwrite = self.capacity[self.hash_index(key)].find(key)
            # checking to make sure this exsist in the linked list
            if overwrite is not None:

                cur = self.capacity[self.hash_index(key)].head
                while cur is not None:
                    if cur.key == key:
                        cur.value = value
                    cur = cur.next
            else:
                self.capacity[self.hash_index(key)].insert_at_head(key, value)
        else:
            linked = LinkedList()
            linked.insert_at_head(key, value)
            self.capacity[self.hash_index(key)] = linked

        load = self.get_load_factor()
        if load > 0.7:
            self.resize(len(self.capacity) * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        if self.capacity[self.hash_index(key)] is not None:
            self.count -= 1
            deletedNode = self.capacity[self.hash_index(key)].delete_node(key)
            return deletedNode
        else:
            return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        if self.capacity[self.hash_index(key)] is not None:
            return self.capacity[self.hash_index(key)].find(key)
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.

        if the load size > .7 -> resize the hash table
        make a new array with double the capacity of the old one
        have a hash table refer to the new array
        run through all the nodes of the old hash table array
            put them in the new hash table
        """
        # Your code here
        old_hash = self.capacity
        self.capacity = [None] * new_capacity
        self.count = 0

        for x in old_hash:
            if x is not None:
                cur = x.head

                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next


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
