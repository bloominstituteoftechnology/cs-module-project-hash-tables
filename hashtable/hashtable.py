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


class LinkedList:
    def __init__(self, key, value):
        new_node = HashTableEntry(key, value)
        self.head = new_node
        self.tail = new_node
        self.size = 0

    def insert(self, key, value):
        new_node = HashTableEntry(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if curr == self.head:
                    self.head = curr.next
                    return
                else:
                    prev.next = curr.next
                    return
            prev = curr
            curr = curr.next

    def get(self, key):
        print('key', key)
        curr = self.head
        while curr:
            if curr.key == key:
                print('match')
                return curr.value
            curr = curr.next
        return None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.hashTable = [None] * capacity
        self.entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hashTable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.entries / self.get_num_slots()

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
        hash = 5381
        for k in key:
            hash = ((hash << 5) + hash) + ord(k)
        return hash

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
        idx = self.hash_index(key)
        if self.get_load_factor() < 0.7:
            if self.hashTable[idx] is None:
                self.hashTable[idx] = LinkedList(key, value)
            else:
                self.hashTable[idx].insert(key, value)
        else:
            if self.hashTable[idx] is None:
                self.hashTable[idx] = LinkedList(key, value)
            else:
                self.hashTable[idx].insert(key, value)
            self.resize(self.get_num_slots() * 2)

        self.entries += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        if self.hashTable[idx]:
            self.hashTable[idx].delete(key)
            self.entries -= 1
        else:
            print('key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        idx = self.hash_index(key)
        if self.hashTable[idx]:
            return self.hashTable[idx].get(key)
        else:
            return None

    def resize(self, new_capacity):
        items = []

        def getListNodes(node):
            if not node:
                return
            items.append([node.key, node.value])
            getListNodes(node.next)
        for item in self.hashTable:
            if item:
                getListNodes(item.head)

        self.hashTable = [None] * new_capacity
        for item in items:
            self.put(item[0], item[1])


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