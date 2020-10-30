

import sys
sys.path.append("../../Data-Structures")
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

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
        # Monday self.ht = [-1]*capacity
        self.slots = [DoublyLinkedList() for i in range(capacity)]
        self.capacity = capacity
        self.num_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.slots)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return 1.0 - ((self.capacity - self.num_items) / self.capacity)

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
        for char in key[1:]:
            hash = (hash << 5) + hash + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value, resize=True):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hi = self.hash_index(key)
        exists = False
        for n in self.slots[hi]:
            if n.value.key == key:
                n.value.value = value
                exists = True
        if not exists:
            entry = HashTableEntry(key, value)
            self.slots[hi].add_to_tail(entry)
            self.num_items += 1
        if resize:
            self.calculate_load()
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hi = self.hash_index(key)
        ll = self.slots[hi]
        for n in ll:
            if n.value.key == key:
                ll.delete(n)
                self.num_items -= 1
                self.calculate_load()
                return
        return "Key not found"
  

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hi = self.hash_index(key)
        ll = self.slots[hi]
        for n in ll:
            if n.value.key == key:
                return n.value.value

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old_slots = self.slots
        self.slots = [DoublyLinkedList() for i in range(self.capacity)]
        for ll in old_slots:
            for n in ll:
                self.put(n.value.key, n.value.value, False)


    def calculate_load(self):
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        elif self.get_load_factor() < 0.2:
            if self.capacity < MIN_CAPACITY * 2:
                self.resize(MIN_CAPACITY)
            else:
                self.resize(self.capacity // 2)

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


