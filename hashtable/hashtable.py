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
    def __init__(self):
        self.head = None

    def get_val(self, val):
        cur = self.head
        while cur is not None:
            if cur.value == val:
                return cur
            cur = cur.next

        return None

    def get_key(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next

        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def delete(self, key):
        if self.head.key == key:
            old_head = self.head
            self.head = self.head.next
            return old_head
        prev = self.head
        cur = prev.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur

            prev = prev.next
            cur = cur.next


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_data = [None] * self.capacity
        self.element_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hash_data)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.element_count / self.capacity

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
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # NAIVE WAY --------------------------------------
        # index = self.hash_index(key)
        # self.hash_data[index] = value
        # self.element_count += 1

        # Way that handles collisions ---------------------------------
        # if the index place is empty - we can just add a new linkedList with this node as the head
        index = self.hash_index(key)
        if self.hash_data[index] is None:
            new_list = LinkedList()
            new_list.insert_at_head(HashTableEntry(key, value))
            # then add the newly-generated LindedList to the index spot just like the naive way
            self.hash_data[index] = new_list
        else:  # if there is some data in the index place, we need to either overwrite or add to the head
            # check to see if the key already exists in the linkedlist or not
            if self.hash_data[index].get_key(key) is None:
                # if the key doesn't exist already, add a new entry to the head of the linked list
                new_entry = HashTableEntry(key, value)
                self.hash_data[index].insert_at_head(new_entry)
            # if the key already exists, we need to overwrite the value to the new value
            else:
                current = self.hash_data[index].head
                while current:
                    if current.key == key:
                        current.value = value
                    current = current.next
            self.element_count += 1

            # resize if the load factor grows to above 0.7
            if self.get_load_factor() >= 0.7:
                self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_data[index] is None:
            print("Key not found")
            return None
        else:
            self.element_count -= 1
            self.hash_data[index].delete(key)

        # resize if the load factory is under 0.2
        if self.get_load_factor() < 0.2 and self.capacity >= 16:
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.hash_data[index].get_key(key):
            lookup = self.hash_data[index].get_key(key)
            return lookup.value

        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
"""

        # establish a new hash table
        prev = self.hash_data
        self.capacity = new_capacity
        self.hash_data = [None] * self.capacity

        # reset element_count
        self.element_count = 0

        # then pass in all of the data that we already had
        for elem in prev:
            if elem:
                current = elem.head
                while current:
                    self.put(current.key, current.value)
                    # then move onto the next one
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
