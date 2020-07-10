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
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        
        self.storage = [None for x in range(self.capacity)]
        self.count = 0
        self.loadfactor = 0

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
        return self.loadfactor

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
        h = 5381

        for char in key:
            h = ((h << 5) + h) + ord(char)

        return h


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
        loc = self.hash_index(key)
        if self.storage[loc] is None:
            # new entry
            self.storage[loc] = HashTableEntry(key, value)
            self.count += 1
            self.loadfactor = self.count / self.capacity
            if self.loadfactor > 0.7:
                self.resize(self.capacity * 2)
        else:
            # check node(s) for same key, replace if same key
            # otherwise add to tail
            cur = self.storage[loc]
            while cur is not None:
                if cur.key == key:
                    cur.value = value
                    return
                # break early so the position in the list
                # isn't lost
                if cur.next is None:
                    break
                cur = cur.next
            # node not found, append to end of list
            cur.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        loc = self.hash_index(key)
        if self.storage[loc] is None:
            # not found
            raise LookupError('key does not exist in hash table')
        else:
            # found, only entry
            if self.storage[loc].next is None:
                self.storage[loc] = None
                self.count -= 1
                self.loadfactor = self.count / self.capacity
                return
            else:
                # traverse down list to delete correct node
                cur = self.storage[loc]
                # check the first node
                if cur.key == key:
                    # remove the head and stop
                    self.storage[loc] = self.storage[loc].next
                    self.count -= 1
                    self.loadfactor = self.count / self.capacity
                    return
                # else, start traversing
                while cur.next is not None:
                    # if the next node is the match, remove it
                    if cur.next.key == key:
                        cur.next = cur.next.next
                        self.count -= 1
                        self.loadfactor = self.count / self.capacity
                        return
                    # keep traversing
                    cur = cur.next
                # wasn't found for whatever reason
                raise LookupError('key was not found at location')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        loc = self.hash_index(key)
        if self.storage[loc] is None:
            return None
        else:
            cur = self.storage[loc]
            # start traversing, check each node as you go along
            while cur is not None:
                # check each node's key as you go along
                if cur.key == key:
                    return cur.value
                cur = cur.next
            # not found at location
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # save old storage, go through each one and re-hash
        old_storage = self.storage.copy()
        # update capacity and storage
        self.capacity = new_capacity
        self.count = 0
        self.storage = [None for x in range(self.capacity)]
        for node in old_storage:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next

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
