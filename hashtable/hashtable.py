from fnvhash import fnv1a_64

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
        # Your code here
        self.capacity = capacity
        self.slots = [None] * MIN_CAPACITY if capacity < 8 else [None] * capacity
        self.items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.slots)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.items / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        return fnv1a_64(str.encode(key))

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_key = self.fnv1(key)
        hash_i = self.hash_index(key)
        if self.slots[hash_i]:
            entry = self.slots[hash_i]
            while entry.next:
                if entry.key == hash_key:
                    return
                entry = entry.next
            entry.next = HashTableEntry(hash_key, value)
        else:
            self.slots[hash_i] = HashTableEntry(hash_key, value)
            self.items += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_key = self.fnv1(key)
        hash_i = self.hash_index(key)
        if self.slots[hash_i]:
            entry = self.slots[hash_i]
            prev = None
            while entry:
                if entry.key == hash_key:
                    if prev == None:
                        self.slots[hash_i] = entry.next
                    else:
                        prev.next = entry.next
                    if self.slots[hash_i] == None:
                        self.items -= 1
                    return
                prev = entry
                entry = entry.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_key = self.fnv1(key)
        hash_i = self.hash_index(key)
        if self.slots[hash_i]:
            entry = self.slots[hash_i]
            while entry:
                if entry.key == hash_key:
                    print(f'key: {entry.key}, value: {entry.value} ')
                    return
                entry = entry.next

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if self.get_load_factor() < 0.7:
            return

        self.capacity = self.capacity * 2
        self.items = 0
        new_slots = [None] * self.capacity

        for slot in self.slots:
            if slot:
                entry = slot
                # print(entry)
                while entry:
                    hash_i = entry.key % self.capacity
                    entry_to_add = entry
                    entry = entry.next
                    if not new_slots[hash_i]:
                        new_slots[hash_i] = entry_to_add
                        entry_to_add.next = None
                    else:
                        new_entry = new_slots[hash_i]
                        while new_entry.next:
                            new_entry = new_entry.next
                        new_entry.next = entry_to_add
                        entry_to_add.next = None
        self.slots = new_slots
        
                



        

        

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

# print(ht.slots[0].value)
ht.delete("line_1")
ht.delete("line_12")
ht.delete("line_9")
ht.delete("line_11")
ht.delete("line_7")
# ht.get("line_3")
# print(ht.slots[0].value)

def show_ht(ht):
    for i, slot in enumerate(ht.slots):
        entry = slot
        print(f'slot {i}')
        if not entry:
            print('no entry')
        while entry:
            print(f'key: {entry.key}, value: {entry.value}')
            entry = entry.next
# show_ht(ht)
ht.resize(16)
show_ht(ht)


# print(ht.fnv1('science'))

# Uncomment code below line 129 to test hash table
# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
