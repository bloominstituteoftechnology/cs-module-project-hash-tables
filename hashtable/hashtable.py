class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"The key is: {self.key}, and the value is: {self.value}"


class LinkedList:

    def __init__(self):
        self.head = None

    def find(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next
        return None

    def insert_at_head(self, node):
        # Link the node to the current HEAD
        node.next = self.head
        # Set head pointer to new node
        self.head = node

    def delete(self, key):
        # Handle the case where the node to delete is the HEAD
        if key == self.head.key:
            self.head = self.head.next
            return self.head

        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return curr

            prev = curr
            curr = curr.next

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
        self.table = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / len(self.table)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        fnv_prime = 16777619
        offset_basis = 2166136261

        # FNV-1a Hash Function
        hashed = offset_basis + key
        for char in self.capacity:
            hashed = hashed * fnv_prime
            hashed = hashed ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        str_key = str(key).encode()
        hash_value = 5381
        for s in str_key:
            hash_value = ((hash_value << 5) + hash_value) + s

        return hash_value & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hashed_index = self.hash_index(key)
        if self.table[hashed_index] is not None:
            pass
        # TODO working on getting linked list to work

        else:
            self.count = self.count + 1
            self.table[hashed_index] = (HashTableEntry(key, value))

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_key = self.djb2(key)
        hashed_index = self.hash_index(hashed_key)
        self.table[hashed_index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hashed_key = self.djb2(key)
        hashed_index = self.hash_index(hashed_key)
        return self.table[hashed_index]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.count == 0:
            self.capacity = new_capacity
            self.table = [None] * self.capacity

        new_table = [None] * new_capacity
        for item in enumerate(self.table):
            if item is None:
                pass
            hashed_key = self.djb2(item)
            hashed_index = self.hash_index(hashed_key)
            new_table.insert(hashed_index, item)

        self.table = new_table


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
